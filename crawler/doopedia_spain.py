import requests
from bs4 import BeautifulSoup


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