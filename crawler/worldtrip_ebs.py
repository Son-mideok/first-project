
'''
3. EBS 세계테마기행 크롤링(셀레니움)
'''

#Select 모듈추가 후 Select() 함수사용

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from re import search


url = 'https://worldtrip.ebs.co.kr/worldtrip/main'
driver.get(url)


# 파이썬 셀레니움 드롭다운 박스 선택
# 셀레니움 드롭다운 select tag xpath로 크롤링 

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

vod_list
