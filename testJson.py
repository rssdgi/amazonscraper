#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:59:42 2019

@author: diego
"""

import json
import os

idDict = {}  
idDict['data'] = '2019-02-02'  
idDict['listname']="my computer"
idDict['amazon']=[]
idDict['amazon'].append({  
    'name': 'cpu',
    'id': 'ABCD',
    'price': '300 EUR'
})
idDict['amazon'].append({  
    'name': 'motherboard',
    'id': 'EFGH',
    'price': '180 EUR'
})
idDict['amazon'].append({  
    'name': 'gpu',
    'id': 'IJKL',
    'price': '230 EUR'
})

if os.path.isfile('data.txt'):
    with open('data.txt') as fobj:
        text = fobj.read()
        fobj.close()

with open('data.txt', 'a') as outfile:  
    if not text.endswith('\n'):
        outfile.write("\n")
    json.dump(idDict, outfile)
    outfile.close()

data=[]
i=0
for line in open('data.txt', 'r') :  
    data.append(json.loads(line))
    i+=1
    print("printing line ",i," value is \n",line)
