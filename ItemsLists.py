# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:36:13 2019

@author: DRossi
object that keeps the lists of items:
attributes:
    _listOfItems-> array of dictionary
    [{"list":"lgnewoled","ids":[{"id":"B07CL963W6","desc":"televisore lg"}]
methods:
    makeListFromFile-> create array _listOfItems from file
    saveListToFile-> save array to file
"""
import json

class ItemsLists:
    def __init__(self):
        self._listsOfItems=[]
        
    def makeListFromFile(self,fileName):
         for line in open(fileName, 'r') :  
            self._listsOfItems.append(json.loads(line))
    
    def getItemsLists(self):
        return self._listsOfItems
    
    def saveListToFile(self,fileName):
        # text is needed to check if file exists
        with open(fileName, 'w') as outfile:
            for f in self.getItemsLists():
                json.dump(f, outfile)
                outfile.write("\n")
            outfile.close()