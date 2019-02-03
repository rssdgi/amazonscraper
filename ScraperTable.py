#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:00:33 2019

@author: diego
class to manage an array of ScraperRow objects
"""

import json

class ScraperTable:
    def _init_(self):
        self._scraperTable=[]
        
    def addRow(self,row):
        self._scraperTable.append(row)
    
    def getTable(self):
        return self._scraperTable
    
    def writeTableToFile(self,fileName):
        # text is needed to check if file exists
        with open(fileName, 'w') as outfile:
            json.dump(self._scraperTable, outfile)
            outfile.close()
        