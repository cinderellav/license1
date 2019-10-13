import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.historyexam.go.kr/pageLink.do?link=examSchedule',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

koreahistories = soup.select('#sub_content > div.right_sider > div.right_contents > table:nth-child(4) > tbody > tr')

for koreahistory in koreahistories:
    koreahistory_date = koreahistory.select_one('tr > td:nth-child(3)')
    if koreahistory_date is not None:
        date = koreahistory_date.text
        print(date)
