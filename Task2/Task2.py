from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os


#launch url
url = "http://www.ycombinator.com/companies/"

## create a new Chrome session
driver = webdriver.Chrome("C:\\Users\Zineb Lahrichi\Desktop\KAIST\dealroom\chromedriver.exe")
driver.implicitly_wait(30)
driver.get(url)


python_button = driver.find_element_by_class_name('name') #FHSU
python_button.click() #click fhsu link
soup=BeautifulSoup(driver.page_source, 'lxml')

##Data storage

name =  []
date = []
description = []
url = []


##Getting name, date and descrpition in the td tags

i = 0

for link in soup.find_all('td'):

    if i == 0 :
        name.append(link.get_text())
        i+=1
        continue
    elif i == 1:
        date.append(link.get_text())
        i+=1
        continue
    elif i == 2 :
        description.append(link.get_text())
        i = 0
        continue


##Going through tr tags to get url in a tags


table = soup.findChildren('table')[0]
rows = table.findChildren('tr')
for row in rows:
    cells = row.findChildren('a')

    if len(cells) == 0:
        url.append('')
    else:
        for cell in cells:
            cell_content = cell.get('href',None)
            url.append(cell_content)


#Making sure all lists have the same shape
#print(len(name), len(date), len(description), len(url))

data = pd.DataFrame()
data['name'] = name
data['date'] = date
data['description'] = description
data['url'] = url

data.to_csv('scraping.csv')
