# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:03:00 2019
programma per aggiornare i prezzi di oggetti amazon
legge gli id degli elementi amazon da file
scarica informazioni da amazon ed aggiorna il file dei risultati
syntax:
    $0 -i fileID -o fileOut
@author: DRossi
"""

from lxml import html
import csv
import datetime
import argparse
import requests
import os
import pandas as pd

def readInputFile(inputFile):
    fp = open(inputFile) # Open file on read mode
    lines = fp.read().split("\n") # Create a list containing all lines
    fp.close() # Close file
    #remove comment lines beginning with #
    return [item for item in lines if item[0]!='#']


def scrapPage(url):
    # get the amazon url for the id
    # and return an array of [name,price]
    
    # open page and get contents
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url,headers=headers)
        doc = html.fromstring(response.content)
        # find name
        XPATH_NAME='//h1[@id="title"]//text()'
        name=doc.xpath(XPATH_NAME)
        #print (response.content)
        # strip empty line from name array
        name=''.join(name).strip()
         # find amazon price
        XPATH_PRICE='//span[contains(@id,"priceblock_dealprice") or contains(@id,"priceblock_ourprice")]//text()'
        price=doc.xpath(XPATH_PRICE)
        price=(''.join(price).strip()).replace(",",".")
        #print("name is ",name," price is ",price)
        return [name,price]
    except Exception as e:
         print (e)
         return []

if __name__ == "__main__":
    
    # manage input arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,help="file con amazon IDs")
    ap.add_argument("-o", "--output", required=True,	help="file per output")
    args = vars(ap.parse_args())
    
    exists = os.path.isfile(args['output'])
    # output file doesn't exist so create it
    if not exists: 
        #createOutFile(args['output'])
        dataframe=None
    else:
        # read out file in dataframe
        dataframe=pd.read_csv(args['output'], sep=';')
        dataframe=dataframe.fillna(0)
        
    
    # set datetime
    # current date and time clear
    currentDate=datetime.datetime.now().strftime("%Y-%m-%d")
    
    # leggi il file degli ID amazon da passare come parametro
    idsArray=readInputFile(args['input'])
    
    # loop for every id
    for id in idsArray:
        resArray=[currentDate]
        resArray=resArray+[id]
        amazonUrl='https://www.amazon.it/dp/'+id+"/"
        print ("Processing page ",amazonUrl)
        resArray=resArray+scrapPage(amazonUrl)
        print (';'.join(resArray))
        # write output to file
   
        # Keep presets
        #csvfile=open(args['output],"a",newline='')
        #writer = csv.writer(csvfile, delimiter=';')
        #writeToCsv(resArray,args{'output})
        # float(re.findall('\d+.*',s)[0]) extract number from strice as float
        # NOTE: the string must not be empty or array fails with out of bound
        
        
    