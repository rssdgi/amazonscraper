#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:03:43 2019

@author: diego
main scraper program
"""


from ScraperRow import ScraperRow
from ScraperTable import ScraperTable
from TableTotals import TableTotals
from ItemsLists import ItemsLists
import datetime

if __name__ == "__main__":
    # read id list 
    idsFile='idsLists.json'
    i=0
    scraperRow=ScraperRow()
    scraperTable=ScraperTable()
    listsOfItems=ItemsLists()
    currentDate=datetime.datetime.now().strftime("%Y-%m-%d")

    listsOfItems.makeListFromFile(idsFile)
    
    # set scraperRow date
    scraperRow.setDate(currentDate)

    for t in listsOfItems.getItemsLists():
        print("processing list ",t['list'])
        scraperRow.setList(t['list'])
        for x in t['ids']:
            print ("getting from amazon id", x['id'], " ",x['desc'])
            scraperRow.scrapItem(x['id'])
        #add to table
        scraperRow.makeDictArray()
        scraperTable.addRow(scraperRow.getRow())
    
    tot=TableTotals(scraperTable.getTable())
    fileout="scraperTable.json"
    scraperTable.writeTableToFile(fileout)