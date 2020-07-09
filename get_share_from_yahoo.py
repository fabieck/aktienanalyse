import requests_html
from bs4 import BeautifulSoup
url = 'https://in.finance.yahoo.com/quote/DAI.DE'
session = requests_html.HTMLSession()
r = session.get(url)
content = BeautifulSoup(r.content, 'lxml')
#print(content)
price = str(content).split('data-reactid="42"')[5].split('</span>')[0].replace('>','')
#price = str(content).split('data-reactid="32"')[4].split('</span>')[0].replace('>','')
print(price)