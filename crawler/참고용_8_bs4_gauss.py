from cgitb import text
from inspect import Attribute
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status() #문제있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text() # 샘플로 첫번째 잘가져오는지 확인 [0]은 리스트니깐 0번째에 해당하는 값
# # td 밑에 a 태그 있는것, a 태그 밑에 있는 text 가져오기 위해서 .a.get.text
# link = cartoons[0].a["href"] # 속성가져오려면 [] 대괄호 쓰기
# # 이왕하는거 카툰 링크 가져와서 클릭되도록 하기
# print(title)
# print("https://comic.naver.com" + link) # 빠진 링크부분도 붙이기


# 웹툰 제목 + 링크 주소
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)


# 웹툰 평점 구하기
