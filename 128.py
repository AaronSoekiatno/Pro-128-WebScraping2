import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

page = requests.get(START_URL)
soup = BeautifulSoup(browser.page_source, 'html.parser')
star_table = soup.find_all('table')
stars_data = []
table_rows = star_table[7].find_all('tr')

header = ['Star name', 'radius', 'mass', 'Distance data']
index = 0
temp_list = []
for tr_tags in table_rows:
            td_tags = tr_tags.find_all("td")
            row = [i.text.rstrip() for i in td_tags]
            if index == 0:
                index +=1
            elif index >=1:
                final_row = [row[0], row[8], row[7], row[5]]
                stars_data.append(final_row)

with open('scrapper2.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(stars_data)

