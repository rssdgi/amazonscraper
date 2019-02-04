#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:03:43 2019

@author: diego
main scraper program
"""

import json
from ScraperRow import ScraperRow

if __name__ == "__main__":
    # read id list 
    idsFile='idsLists.json'
    itemsIds=[]
    i=0
    scraperRow=ScraperRow()

    for line in open(idsFile, 'r') :  
        itemsIds.append(json.loads(line))
    
    for t in itemsIds:
        print("processing list ",t['list'])
        for x in t['ids']:
            print ("getting from amazon id", x['id'], " ",x['desc'])
            scraperRow.scrapItem(x['id'])
        