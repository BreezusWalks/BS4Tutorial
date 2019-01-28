import bs4 as bs
import urllib.request as req

source = req.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

print()

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

print()

for url in soup.find_all('a'):
    print(url.get('href'))

print()

print(soup.get_text())