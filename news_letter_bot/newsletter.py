# 메일할지 말지

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from re import search



# 네이버 스페인 백과사전 크롤링
URL = 'https://terms.naver.com/entry.naver?docId=1125333&cid=40942&categoryId=34081'
response = requests.get(URL)
soup =BeautifulSoup(response.text, 'html.parser')

spain_tbody = soup.select_one('tbody')
trs = spain_tbody.select('tr')

spain_result = {}

for tr in trs:

    spain_title = tr.select('th > span')[0].text.strip()
    spain_data = tr.select('td')[0].text.strip()
    
    spain_result.setdefault(spain_title, spain_data)

print(spain_result)


# 세계테마기행 셀레니움


url = 'https://worldtrip.ebs.co.kr/worldtrip/main'
driver.get(url)

driver.implicitly_wait(3)
dropdown = Select(driver.find_element(By.ID,'catgry1'))  #정렬기준 드롭다운
dropdown.select_by_visible_text('세계테마기행')

driver.implicitly_wait(3)
dropdown2 = Select(driver.find_element(By.ID,'catgry2'))
dropdown2.select_by_visible_text('유럽')

driver.implicitly_wait(3)
dropdown3 = Select(driver.find_element(By.ID,'catgry3'))
dropdown3.select_by_visible_text('스페인')


driver.implicitly_wait(3)
# search = driver.find_element(By.CLASS_NAME, 'submit')
# driver.click()
try:
    driver.find_element(By.CSS_SELECTOR, 'a[onclick^="catgrySearch( this )"]').click() 
except:
    driver.find_element(By.CSS_SELECTOR, 'a[onclick^="catgrySearch(this)"]').click()

element = driver.find_element(By.XPATH, '//*[@id="vodList"]/li[1]/a/span/span/span[1]')

elements = driver.find_elements(By.CSS_SELECTOR, '#vodList > li > a')

elements=elements[:10]

vod_list = []

for element in elements:
    title = element.text
    link = element.get_attribute('href')

#print(title,link)

    temp = {}
    temp['동영상 제목'] = title
    temp['링크'] = link

    vod_list.append(temp)

print(vod_list)


#C:\Users\virtue\Desktop\virtue_package\newsletter.html 경로 파악하기
/home/ubuntu/project/template/dailyfood.html

file = open("", "w", encoding= 'utf-8')
string = '''<body style="background-color:#2D2D2D;">


file.write(string + div)
file.close()