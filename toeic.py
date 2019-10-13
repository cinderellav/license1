import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://appexam.ybmnet.co.kr/toeic/info/receipt_schedule.asp',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

toeics = soup.select('#pDiv table tr')

for toeic in toeics:
    toeic_date = toeic.select_one('tr:nth-child(2) td:nth-child(2)')
    if toeic_date is not None:
        date = toeic_date.text
        print(date)

