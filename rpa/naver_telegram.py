# 1. 네이버 사전 검색 크롤링: 스페인 국가 주요정보

import requests
from bs4 import BeautifulSoup


URL = 'https://terms.naver.com/entry.naver?docId=1125333&cid=40942&categoryId=34081'
response = requests.get(URL)
soup =BeautifulSoup(response.text, 'html.parser')

spain_tbody = soup.select_one('tbody')
trs = spain_tbody.select('tr')

for tr in trs:

    spain_title = tr.select('th > span')[0].text.strip()
    spain_data = tr.select('td')[0].text.strip()
    
    spain_result.setdefault(spain_title, spain_data)
spain_result

final_result='원어명: '+ spain_result['원어명'] + '위치: '+ spain_result['위치']+ '시간대: '+spain_result['시간대'] +'면적(㎢): '+ spain_result['면적(㎢)']+'시간대: '+spain_result['시간대']+'수도: '+spain_result['수도']+'종족구성: '+spain_result['종족구성']+'국제전화: '+spain_result['국제전화']


# 2. 텔레그램으로 내용 전송

import telegram
telegram_config = {}
with open(r'C:\Users\virtue\Desktop\telegram_config', 'r') as f: # config 한줄씩 읽어온다
    configs = f.readlines()
    for config in configs:
        key, value = config.rstrip().split('=')
        telegram_config[key] = value


token = telegram_config['token']

bot = telegram.Bot(token) 
updates = bot.get_updates()
chat_id = updates[-1].message.chat.id

bot.send_message(chat_id, '스페인 주요정보입니다.')
bot.send_message(chat_id, final_result)