#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:00:33 2019

@author: diego
class to manage an array of ScraperRow objects
attributes:
_scraperTable-> array of rows objects
methods:
    addRow-> get a row and add it (copy it) to the _scraperTable
    getTable-> return the _scraperTable object
    writeTableToFile-> write _scraperTable object to file 
    readTableFromFile-Z read __scraperTable object from file 
"""
import copy
import json

class ScraperTable:
    def __init__(self):
        self._scraperTable=[]
        
    def addRow(self,row):
        #append copy reference to object, we need to copy it
        self._scraperTable.append(copy.copy(row))
    
    def getTable(self):
        return self._scraperTable
    
    def writeTableToFile(self,fileName):
        # text is needed to check if file exists
        with open(fileName, 'w') as outfile:
            for f in self.getTable():
                json.dump(f, outfile)
                outfile.write("\n")
            outfile.close()
    
    def readTableFromFile(self,fileName):
        # text is needed to check if file exists
        for line in open(fileName, 'r') :  
            self._scraperTable.append(json.loads(line))
        
        
        