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
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
from selenium import webdriver
import re
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


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
        #f.write(data1)
print("\n Now scraping on Amazon.....\n It is usually slower than Myntra......")

options = Options()
options.headless = True

ua = UserAgent()
a = query.split()
query_str = ''

for index, i in enumerate(a):
    if index == 0:
        query_str += i
    else:
        query_str = query_str + '+' + i

amazn_search = 'https://www.amazon.com/s?k=' + query_str + '&ref=nb_sb_noss_2'
browser = webdriver.Firefox(options=options)
browser.get(amazn_search)
headers = {'User-Agent': str(ua.google)}


soup = BeautifulSoup(browser.page_source, 'html.parser')


link_1 = 'https://www.amazon.com'
productlink_tags = soup.find_all('a', attrs={'class': 'a-link-normal a-text-normal'})

productlinks = [i['href'] for i in productlink_tags]

names = []
prices = []



for index, ina in enumerate(productlinks):
    if index ==3:
        break
    ina = link_1 + ina
    print(ina)
    headers = {'User-Agent': str(ua.random)}
    # product_html = requests.get(ina, headers=headers).text
    browser.get(ina)

    namenprice_ele = [['//*[@id="productTitle"]', '//*[@id="priceblock_dealprice"]'],
                      ['//*[@id="productTitle"]', '//*[@id="priceblock_ourprice"]'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[4]/div/div/div[2]/form[2]/button'],
                      ['//*[@id="productTitle"]', '/html/body/div[2]/div[1]/div[4]/div[5]/div[9]/div/div[2]/ul/li[4]/span/span[1]/span/a/span[2]/span'],
                      ['//*[@id="productTitle"]', '/html/body/div[2]/div[1]/div[4]/div[5]/div[9]/div/div[2]/ul/li[2]/span/span[1]/span/a/span[2]/span'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[4]/div/div/div[2]/form[2]/button'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[5]/div/div/div[2]/form[2]/button'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[5]/div/div/div[1]/div/div/strong'],
                      ['//*[@id="productTitle"]', '/html/body/div[2]/div[1]/div[4]/div[6]/div[13]/div/div[1]/ul/li[2]/span/span/span/a/span[2]/span'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[4]/div/div/div[1]/div/div/strong'],
                      ['/html/body/div[1]/div[3]/div/div/section/h1', '/html/body/div[1]/div[3]/div/div/section/div[4]/div/div/div[1]/div/div/strong'],
                      ['//*[@id="productTitle"]', '/html/body/div[2]/div[1]/div[4]/div[6]/div[12]/div/div[1]/ul/li/span/span/span/a/span[2]/span']

                      ]

    for f in namenprice_ele:

        try:
            name = browser.find_element_by_xpath(f[0])
            price = browser.find_element_by_xpath(f[1])
        except:
            continue

        if name.text and price.text:
            print(">>" + name.text)
            k = re.search('\$.*$', price.text).group()
            print('>>'+k)
        else:
            price('not compatible')
        break






print("Calculating recommendations for...    " + stringg+":")

pd.set_option('display.max_columns', 100)
newdataframe = pd.read_csv('c.csv', encoding ="UTF8")
newdataframe.head()



newdataframe.shape



newdataframe = newdataframe[['Title','Genre','Director','Actors','Plot']]
newdataframe.head()




newdataframe.shape




newdataframe['Actors'] = newdataframe['Actors'].map(lambda x: x.split(',')[:3])
newdataframe['Genre'] = newdataframe['Genre'].map(lambda x: x.lower().split(','))
newdataframe['Director'] = newdataframe['Director'].map(lambda x: x.split(' '))


for index, row in newdataframe.iterrows():
    row['Actors'] = [x.lower().replace(' ','') for x in row['Actors']]
    row['Director'] = ''.join(row['Director']).lower()







newdataframe['Key_words'] = ""

for index, row in newdataframe.iterrows():
    plot = row['Plot']
    
    rake_instance = Rake()

    rake_instance.extract_keywords_from_text(plot)

    key_words_dict_scores = rake_instance.get_word_degrees()

    row['Key_words'] = list(key_words_dict_scores.keys())


newdataframe.drop(columns = ['Plot'], inplace = True)




newdataframe.set_index('Title', inplace = True)
newdataframe.head()




newdataframe['bow'] = ''
columns = newdataframe.columns
for index, row in newdataframe.iterrows():
    words = ''
    for col in columns:
        if col != 'Director':
            words = words + ' '.join(row[col])+ ' '
        else:
            words = words + row[col]+ ' '
    row['bow'] = words
    
newdataframe.drop(columns = [col for col in newdataframe.columns if col!= 'bow'], inplace = True)




newdataframe.head()




count = CountVectorizer()
cmatrix = count.fit_transform(newdataframe['bow'])

point = pd.Series(newdataframe.index)
point[:5]





cs = cosine_similarity(cmatrix, cmatrix)
cs




def recommendations(title, cosine_sim = cs):
    
    r = []
    
    
    idx = point[point == title].index[0]

    #similarity scores in descending order
    ss = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    
    top10 = list(ss.iloc[1:11].index)
    
    for i in top10:
        r.append(list(newdataframe.index)[i])
        
    return r




x=recommendations(stringg)
print (*x, sep= "\n")
