
'''
You should already know how to write a Python script that retrieves an arbitrary
Wikipedia page and produces a list of links on that page:
'''
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

'''--------------------------------------------------------------------------------------------------'''

'''
You can use these rules to revise the code slightly to retrieve only the desired article
links by using the regular expression ^(/wiki/)((?!:).)*$"):
'''
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''
'''If you run this, you should see a list of all article URLs that the Wikipedia article on
Kevin Bacon links to.'''
'''-------------------------------------------------------------------------------------------------'''

'''
Of course, having a script that finds all article links in one, hardcoded Wikipedia arti‐
cle, while interesting, is fairly useless in practice. You need to be able to take this code
and transform it into something more like the following:

• A single function, getLinks, that takes in a Wikipedia article URL of the
form /wiki/<Article_Name> and returns a list of all linked article URLs in the
same form.

• A main function that calls getLinks with a starting article, chooses a random
article link from the returned list, and calls getLinks again, until you stop the
program or until no article links are found on the new page.

Here is the complete code that accomplishes this:
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import time
import random
import re

random.seed(time.time())
def getLinks(articlUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articlUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

