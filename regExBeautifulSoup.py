from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''
The solution is to look for something identifying about the tag itself. In this case, you
can look at the file path of the product images:
'''
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#RegEx
images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])

