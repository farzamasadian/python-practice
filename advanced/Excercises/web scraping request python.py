import requests
from bs4 import BeautifulSoup
r=requests.get('https://divar.ir/s/tehran')
print(r)

result=r.text
soup=BeautifulSoup(result,'html.parser')

a=soup.find('h2', attrs={'itemprop':'name'})
print(a)
