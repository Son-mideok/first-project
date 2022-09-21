# 셀레니움 드롭다운 함수 선택
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 항공권에서 썼던 함수 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 강의자료 Webdriver Manager 설치할지말지
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(
service=Service(ChromeDriverManager().install()) )

#오류뜰때 코드추가
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_path =r'C:\Users\virtue\Desktop\python_youtube\chromedriver.exe'
browser = webdriver.Chrome(chrome_path)

def main():

    driver = webdriver.Chrome('c:\\chromedriver.exe')
    driver.implicitly_wait(3)

    url = 'https://worldtrip.ebs.co.kr/worldtrip/main'
    driver.get(url)
    driver.implicitly_wait(3)

    dropdown = Select(driver.find_element_by_xpath('//*[@id="section0"]'))  #정렬기준 드롭다운


    #case1 - 인덱스 기준으로 찾기
    
    dropdown.select_by_index(0)
    driver.implicitly_wait(3)

    # '세계테마기행' 텍스트 선택
    driver.find_element_by_xpath('//*[@id="catgry1"]').send_keys('세계테마기행')
    driver.implicitly_wait(3)


     # '유럽' 텍스트 선택
    dropdown.select_by_index(1)
    driver.implicitly_wait(3)

   
    driver.find_element_by_xpath('//*[@id="catgry2"]').send_keys('유럽') 
    driver.implicitly_wait(3)


    # '스페인' 텍스트 선택
    driver.find_element_by_xpath('//*[@id="catgry3"]').send_keys('스페인') 
    driver.implicitly_wait(3)



    #case2 - 실제 텍스트 기준으로 찾기
    #dropdown.selec_by_visible_text("경력순")

    #case3 - <option value> 값으로 찾기
    #dropdown.select_by_value("5")

    #검색 버튼 클릭
    driver.find_element_by_xpath('//*[@id="catgryForm"]').click()    
    driver.implicitly_wait(3)

	#창 유지를 위한 무한 반복문
    while True :
        pass

if __name__ == "__main__":
    main()
