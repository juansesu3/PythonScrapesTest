from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#Dealing with parents
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())



'''If you want to find only descendants that are children, you can use the .children
tag:'''
#for child in bs.find('table', {'id': 'giftList'}).children:
#   print(child)



'''The BeautifulSoup next_siblings() function makes it trivial to collect data from
tables, especially ones with title rows:'''
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
