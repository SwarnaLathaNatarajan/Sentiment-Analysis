from bs4 import BeautifulSoup
import urllib.request
url = 'http://kt.ijs.si/data/Emoji_sentiment_ranking/'
f = open('emoji.txt', 'w', encoding='utf-8')
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page)

table = soup.find('table')
rows = table.findAll('tr')

for tr in rows:
    cols = tr.findAll('td')
    i = 0
    for c in cols:
        i = i+1
        if(i == 1 or i == 3 or i == 9):
            f.write(c.text + ',')
            print(c.text, end=',')
    f.write('$')
    f.write('\n')
    print()


