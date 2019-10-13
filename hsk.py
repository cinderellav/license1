import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.hsk.ne.kr/apply/step00.htm?t=4',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

hsks = soup.select('#aside4 > div:nth-child(3) > div:nth-child(32) > table:nth-child(2) > tbody > tr')
print(hsks)

#aside4 > div:nth-child(3) > div:nth-child(31)
#aside4 > div:nth-child(3) > div:nth-child(32) > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(1)