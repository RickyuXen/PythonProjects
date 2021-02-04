from bs4 import BeautifulSoup
import requests

source = requests.get('https://myanimelist.net/').text
soup = BeautifulSoup(source, 'lxml')
TopAiring = soup.find('div', class_='widget airing_ranking right')

for TopAnime in TopAiring.find_all('li', class_='ranking-unit'):
    for a in TopAnime.p.find_all('a', href=True):
        print(a['href'])
    
topUpcomming = soup.find('div', class_='widget upcoming_ranking right')

for Upcomming in topUpcomming.find_all('li', class_='ranking-unit'):
    for a in Upcomming.p.find_all('a', href=True):
        print(a['href'])