import bs4 as bs
import urllib.request
import pandas as pd

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

#table = soup.find('table')
table = soup.table

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [content.text for content in td]
    print(row)

print()

dataFrames = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dataFrames:
    print(df)

print()

sourceXML = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml')
soupXML = bs.BeautifulSoup(sourceXML, 'xml')
for url in soupXML.find_all('loc'):
    print(url.text)