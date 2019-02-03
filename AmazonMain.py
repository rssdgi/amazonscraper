#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 20:03:43 2019

@author: diego
main scraper program
"""

import json
from ScraperRow import *

if __name__ == "__main__":
    # read id list 
    idsFile='idsLists.json'
    itemsIds=[]
    i=0
    for line in open(idsFile, 'r') :  
        itemsIds.append(json.loads(line))
        
    scraperRow=ScraperRow()
    for t in itemsIds[0]['ids']:
        print ("getting from amazon id", t['id'], " ",t['desc'])
        scraperRow.scrapItem(t['id'])