from cgitb import text
from inspect import Attribute
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status() #문제있으면 프로그램 종료



soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기, a태그에 ~
cartoons =soup.find_all("a", attrs={"class":"title" }) # find 는 조건에 해당하는 첫번째 조건, 해당하는 모든 조건

#반복문으로 리스트 반환, class 속성이 title 인 모든 "a" element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())
