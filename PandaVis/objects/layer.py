#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from objects.corticalColumn import cCorticalColumn
from panda3d.core import NodePath, PandaNode, TextNode


class cLayer:
    def __init__(self, name, nOfColumns, nOfCellsPerColumn):

        self.name = name
        self.nOfCellsPerColumn = nOfCellsPerColumn
        self.corticalColumns = []
        for i in range(nOfColumns):
            c = cCorticalColumn(name, nOfCellsPerColumn)
            self.corticalColumns.append(c)

    def CreateGfx(self, loader):

        self.__node = NodePath(
            PandaNode(self.name)
        )  # TextNode('layerText')#loader.loadModel("models/teapot")

        text = TextNode("Layer text node")
        text.setText(self.name)

        textNodePath = self.__node.attachNewNode(text)
        textNodePath.setScale(2)

        textNodePath.setPos(0, -5, 0)

        self.__node.setPos(0, 0, 0)
        self.__node.setScale(1, 1, 1)

        y = 0
        idx = 0
        row = 0
        for c in self.corticalColumns:
            c.CreateGfx(loader, idx)
            idx += 1
            c.getNode().setPos(row * 10, y, 0)
            y += 3

            if y > 150:
                y = 0
                row += 1
            c.getNode().reparentTo(self.__node)

        return

    def UpdateState(self, activeColumns, winnerCells, predictiveCells):

        # print("COLUMNS SIZE:"+str(len(self.corticalColumns)))
        print("winners:"+str(winnerCells))
        print("predictive:"+str(predictiveCells))
        
        for colID in range(len(self.corticalColumns)):# go through all columns    
            oneOfCellPredictive=False
            
            for cellID in range(len(self.corticalColumns[colID].cells)):
                isActive = cellID+(colID*self.nOfCellsPerColumn) in winnerCells
                isPredictive = cellID+(colID*self.nOfCellsPerColumn) in predictiveCells
                if isPredictive:
                    oneOfCellPredictive=True
                self.corticalColumns[colID].cells[cellID].UpdateState(active = isActive, predictive = isPredictive)

            self.corticalColumns[colID].UpdateState(bursting=False, oneOfCellActive=(colID in activeColumns),oneOfCellPredictive=oneOfCellPredictive)
        
        
#        for cellID in winnerCells:
#            self.corticalColumns[(int)(cellID/self.nOfCellsPerColumn)].cells[(int)(cellID%self.nOfCellsPerColumn)].UpdateState(active = True, predictive = False)
#        
#        for cellID in predictiveCells:
#            self.corticalColumns[(int)(cellID/self.nOfCellsPerColumn)].cells[(int)(cellID%self.nOfCellsPerColumn)].UpdateState(active = True, predictive = True)
        

    def updateWireframe(self, value):
        for col in self.corticalColumns:
            col.updateWireframe(value)
            
    def getNode(self):
        return self.__node

    def DestroyProximalSynapses(self):
        for col in self.corticalColumns:
            col.DestroyProximalSynapses()
    
    def DestroyDistalSynapses(self):
        for col in self.corticalColumns:
            col.DestroyDistalSynapses()
            
    def setTransparency(self,transparency):
        self.transparency = transparency
        for col in self.corticalColumns:
            col.setTransparency(transparency)