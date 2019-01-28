import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source,'lxml')

js_test = soup.find('p', class_='jstest')

print(js_test.text)

#UNABLE TO GET PYQT WORKING