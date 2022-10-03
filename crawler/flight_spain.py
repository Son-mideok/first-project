from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_path =r'C:\Users\virtue\Desktop\python_youtube\chromedriver.exe'
browser = webdriver.Chrome(chrome_path)
# browser = webdriver.Chrome(options=options)

def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

url = 'https://flight.naver.com/'
browser.get(url)

# 함수화(가는날, 오는날)
def flight(departure, arrival_date):
    begin_date = browser.find_element(By.XPATH, '//button[text() =  "가는 날"]')
    begin_date.click()

    #가는 날짜
    wait_until('//b[text() = '+str(departure)+']') # 나올때까지 30초 대기
    browser.find_elements(By.XPATH, '//b[text() = '+str(departure)+']')[0].click()
    

    # 도착 날짜
    wait_until('//b[text() = '+str(arrival_date)+']')
    browser.find_elements(By.XPATH, '//b[text() = '+str(arrival_date)+']')[0].click()


    wait_until('//b[text() = "도착"]')
    arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
    arrival.click()

    wait_until('//button[text() = "유럽"]')
    uro  = browser.find_element(By.XPATH, '//button[text() = "유럽"]')
    uro.click()

    wait_until('//i[contains(text(), "바르셀로나")]')
    spain_BCN = browser.find_element(By.XPATH, '//i[contains(text(), "바르셀로나")]')
    spain_BCN.click()

    wait_until('//span[contains(text(), "항공권 검색")]')
    search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
    search.click()

    elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
    '//div[@class="concurrent_ConcurrentItemContainer__2lQVG result"]')))  # 어짜피 로딩끝나고 대기니깐 def 안씀

    return elem