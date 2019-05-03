import os
import sys
import threading
import urllib.request, urllib.parse, urllib.error,urllib.request,urllib.error,urllib.parse,http.cookiejar
import smtplib
import ftplib
import datetime,time
import bs4
import re
import csv
import numpy
from PIL import Image
import random
from bs4 import BeautifulSoup as soup
import pandas as pd
import string
import html
import requests

query = input('What do I search for: ')
stringg=query


site = "https://www.myntra.com/amp/"+query+"?rows=100&p=1" 

hdr1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr3 = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr4 = {'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr5 = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])
req = urllib.request.Request(site, headers=hdr)


cj_temp = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj_temp)) 
response = opener.open(req)
content = response.read()
response.close()


page_soup = soup(content,"html.parser")
info  = page_soup.findAll("div",{"class" : "productInfo"})
pqr  = page_soup.findAll("div",{"class" : "product"})

y = len(info)
print("Looking in myntra now:\nNumber of pg results=")
print(y)

a = 2
n = 1

while ((y != 0) and (n<=1)) :

    for entry in info[:3]:
    

        product_name = entry.findAll("h4",{"class" : "name-product"})
        product_name = product_name[0].text.strip()
        product_name = str(product_name.encode('utf-8', 'replace'))
        
        brand = entry.findAll("div",{"class" : "name"})
        brand = brand[0].text
        brand = str(brand.encode('utf-8', 'replace'))

        cp = entry.findAll("span",{"class" : "price-discounted"})
        cp = cp[0].text
        cp = str(cp.encode('utf-8', 'replace'))
        cp = cp[3:] 
        op = str(entry.findAll("span",{"class" : "price"}))
        op = str([int(s) for s in op.split() if s.isdigit()])

        op.strip('[]')
        if op and not op.isspace(): 
            pass
        else :
            op = cp


        print( "product name: " + product_name.strip('b'))
        print("brand: " +brand.strip('b'))
        
        print("price : Rs." +op.strip('[]'))
        n=n+1
        data1 = product_name + "," + brand + "," + cp + "," + op + "\n"
