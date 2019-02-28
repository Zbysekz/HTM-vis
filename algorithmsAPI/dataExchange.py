#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 02:33:11 2019

@author: osboxes
"""
from enum import Enum

class ClientData(object):
  def __init__(self):
    self.a = 0
    self.b = 0

class ServerData(object):
  def __init__(self):
    self.inputsValueString = [] #ordinary expressed value that is represented by SDRs
    self.inputs = []
    self.activeColumnIndices=[]
    self.activeCells=[]
    self.columnDimensions=0
    self.cellsPerColumn=0
    
    self.compensateSize=[]#to compensate size by dummy bytes
   
    
class CLIENT_CMD(Enum):
  QUIT = 0
  REQ_DATA = 1
  CMD_RUN = 2
  CMD_STOP = 3
  CMD_STEP_FWD = 4
  
class SERVER_CMD(Enum):
  SEND_DATA = 0
  NA = 1