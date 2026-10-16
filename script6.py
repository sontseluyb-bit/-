import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
nazvy = []
response = requests.get(url)
soup = BeautifulSoup( response.text ,'html.parser')
zag = soup.find('h1').text
naz = soup.find_all('a', title=True)
cina = soup.findAll('p', class_='price_color' )
print(zag)
for i in range(5):
    txt = str(naz[i])
    start = txt.split('title="')[1]
    finish = start.split('"')[0]
    nazvy.append(finish)
    nazvy.append("              ")


print (nazvy)
print(cina[0 : 5])
