'''
Created on 18/11/2013

@author: matlock
'''

import unittest
from src.Memory import *
from src.Frame import *
from src.MMU import *
from src.Instruction import *
from src.Program import *
from src.PCB import *
from src.Kernel import *
from src.Algorithm import *
from src.Scheduler import *

class testKernel(unittest.TestCase):
    
    
    def setUp(self):
        self.instruction1 = BasicInstruction()     
        self.memory = Memory()
        self.memory.buildMemory(5)
        self.frame1 = Frame(self.memory,0,1)
        self.frame2 = Frame(self.memory,1,2)
        self.frame3 = Frame(self.memory,3,1)
        self.frame4 = Frame(self.memory,4,1)
        self.mmu = MMU()
        self.mmu.fullFrames.append(self.frame1)
        self.mmu.fullFrames.append(self.frame2)
        self.mmu.emptyFrames.append(self.frame3)
        self.mmu.emptyFrames.append(self.frame4)
        self.program = Program('a')
        self.program.addInstruction(self.instruction1)
        self.pcbA = PCB('a',0,0,1)
        self.programb = Program('b')
        self.pcbB = PCB('b',0,3,1)
        self.programb.addInstruction(self.instruction1)
        self.frame1.load(self.pcbA,self.program)
        self.frame2.load(self.pcbB,self.programb)
        self.programc = Program('c')
        self.programc.addInstruction(self.instruction1)
        self.programc.addInstruction(self.instruction1)
        self.programc.addInstruction(self.instruction1)
        self.scheduler = Scheduler(PFIFO())
        self.kernel = Kernel (None,None,self.scheduler,self.mmu)
        
        
    def testsaveProgram(self):
        self.kernel.saveProgram(self.programc)
        for i in range(0,5):
            instruction = self.memory.blocks[i]
            self.assertIsInstance(instruction, BasicInstruction, "Compact test")
        
    