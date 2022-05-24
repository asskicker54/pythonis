import requests
import random
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/page/1/'

q = []
a = []
new_url = url

while new_url:
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, "html.parser")
    a += soup.find_all('small', class_='author')
    q += soup.find_all('span', class_='text')
    next = soup.find('li', class_='next')
    if next:
        next_url = next.find('a', href=True)['href']
        new_url = url.replace('/page/1/', next_url)
    else:
        new_url = None

result = random.sample(q, 5)
for quote in result:
    print(quote.text, end='\n')