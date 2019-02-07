#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:43:34 2019

@author: diego
ScraperRow Class
Object that manage amazon scraping process
- attributes: 
rowDict -> dictionary with date, list, items: [{name, price, id}]
{"data": "2019-02-01", "listname": "my computer", "amazon": [{"name": "cpu", "id
": "ABCD", "price": "300 EUR"}, {"name": "motherboard", "id": "EFGH", "price": "
180 EUR"}, {"name": "gpu", "id": "IJKL", "price": "230 EUR"}]}
- methods:
scrapItem get an amazon id, scrap amazon page and create dictionary array with results
self.__itemsDictAr=[{name:, price:, id:}]
setDate-> set date to rowDict
setList-> set list to rowDict
makeDictArray-> add the items arrray to the rowDict
each scraperRow obj keeps only 1 row. Use ScraperTable obj to manage array of rows
"""

import requests
from lxml import html
import re

class ScraperRow:
    def __init__(self):
        print("Initializing ScraperRow")
        self._rowDict={}
        self._itemsDictAr=[]
        self.XPATH_NAME='//h1[@id="title"]//text()'
        self.XPATH_PRICE='//span[contains(@id,"priceblock_dealprice") or contains(@id,"priceblock_ourprice")]//text()'
        self._url='https://www.amazon.it/dp/'
        
    def scrapItem(self,id):
        # open page and get contents
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            url=self._url+id+"/"
            #print ("Quering page ",url)
            response = requests.get(url,headers=headers)
            doc = html.fromstring(response.content)
            # find name
            name=doc.xpath(self.XPATH_NAME)
            #print (response.content)
            # strip empty line from name array
            name=''.join(name).strip()
            #remove any char that is not in the [] domain
            name = re.sub('[^0-9a-zA-Z ]+', '', name)
            name = re.sub('  +', '', name) #remove trailing spaces
            # find amazon price
            pricestr=doc.xpath(self.XPATH_PRICE)
            pricestr=(''.join(pricestr).strip()) #.replace(",",".")
            price=""
            currency=""
            if pricestr:
                price=re.search(r'\d+.{0,1}\d+,{0,1}\d*', pricestr).group()
                currency=re.search(r'\w{1,3}', pricestr).group()
            print("id ",id," name is ",name," price is ",pricestr)
            itemsDict={}
            itemsDict['name']=name
            itemsDict['id']=id
            itemsDict['price']=price
            itemsDict['currency']=currency
            self._itemsDictAr.append(itemsDict)
        except Exception as e:
            print (e)
        
    def setDate(self,date):
        self._rowDict['date']=date
    def setList(self,listname):
        self._rowDict['list']=listname
        # adds the self._idDict object to idsArray 
    def makeDictArray(self):
        # if the id has been scraped
        #if self._idDict['id'] not in [x for v in self._itemsDictAr for x in v.values()]:
        self._rowDict['items']=self._itemsDictAr
        self._itemsDictAr=[]
    def getRow(self):
        return self._rowDict

