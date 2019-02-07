# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:49:16 2019

@author: DRossi
object that keeps track of total price of a list at a specific date
attributes:
    _totals-> array of dictionary to keep the total price for a list|date
    [{'list': 'lgnewoled', 'date': '2019-02-05', 'total': 1270.0, 'nopriced': []}]
    'nopriced' key keeps track of items id with price=0
methods:
    __init__-> expects a table object and create the associated _totals
    addRowTotals-> get a row obj and add it to the _totals or update if list|date exists
"""

import copy

class TableTotals:
     
    def __init__(self,table):
        # crea dictionary {data: list: total:} from row[index]
        self._totals=[]
        for row in table: # loop for each row
            self.addRowTotals(row)
        
    def getTotals(self):
        return self._totals
    
    def addRowTotals(self,row):
        tempDict={}
        total=0
        nopriced=[]
        for i in row['items']: # loop for each row items array
            if i['price']:
                total+=self._convertPriceToFloat(i['price'])
            else:
                nopriced.append(i['id'])
        tempDict['list']=row['list']
        tempDict['date']=row['date']
        tempDict['total']=float("{0:.2f}".format(total))
        tempDict['nopriced']=nopriced
        rowCheck=self._newElementExists(tempDict)
        if not rowCheck[0]:
            self._totals.append(copy.copy(tempDict))
        else:
            self._totals[rowCheck[1]]=copy.copy(tempDict)
    
    def _convertPriceToFloat(self,s):
        # convert string 1.270,99 in float
        s=s.replace('.','').replace(',','.')
        return float(s)
    
    def _newElementExists(self,totalsRow):
        # check if a row of totals already exists in the _totals array
        # returns array [True,index] if exists else [False,0]
        listKey='list'
        dateKey='date'
        for i in range(len(self.getTotals())):
            row=self._totals[i]
            if row[listKey]==totalsRow[listKey] and row[dateKey]==totalsRow[dateKey]:
                return [True,i]
        return [False,0]