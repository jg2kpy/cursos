import bs4
import requests

'''

res = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('html body div.document div.documentwrapper div.bodywrapper div.body div#beautiful-soup-documentation.section h1')
print(elems[0].text.strip())

'''

def getTitle(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body div.document div.documentwrapper div.bodywrapper div.body div#beautiful-soup-documentation.section h1')
    return elems[0].text.strip()

titulo = getTitle('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
print(titulo)