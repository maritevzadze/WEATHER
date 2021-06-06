import requests
from bs4 import BeautifulSoup
from random import randint
import csv

payload = {'groups': 'top_250', 'start':1}
h = {'Accept-Language': 'en-US'}

url = 'https://www.imdb.com/search/title/?genres=action'

file = open("movies.csv", "a")
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Year', 'Ranking'])

while payload['start']<250:
    r = requests.get(url, params=payload, headers=h)
    print(r.url)
    print(r.headers)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    print(soup)
    block = soup.find('div', {'id': 'wrapper'})

    all_movies = block.find_all('div', id_='wrapper')



    for each in all_movies:
        title = each.h3.a.text
        year = each.find('span', id_='wrapper').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        year = year.replace('I', '')

        rating = each.strong.text
        print(rating)
        file_obj.writerow([title, year, rating])
        payload['start'] += 25


