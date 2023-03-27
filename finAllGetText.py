
'''÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://ch.talent.com/jobs?k=&l=Lausanne%2C+Vaud&source=home&context=&id=99853e838b87')
bs = BeautifulSoup(html.read(), 'html.parser')

'''BeautifulSoup’s find() and find_all() are the two functions you will likely use the
most. With them, you can easily filter HTML pages to find lists of desired tags, or a
single tag, based on their various attributes.

Sintaxys
find_all(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)

'''
#nameList = bs.find_all('span', {'class':{'green','red'}})
nameList = bs.find_all('section', {'class':'card card__job'})

'''
The text argument is unusual in that it matches based on the text content of the tags,
rather than properties of the tags themselves. For instance, if you want to find the
number of times “the prince” is surrounded by tags on the example page, you could
replace your .find_all() function in the previous example with the following lines:

nameList = bs.find_all(text='the prince')
print(len(nameList))
'''


'''
#For instance, the following two lines are identical:
bs.find_all(id='text')
bs.find_all('', {'id':'text'})

'''


for name in nameList:
    '''.get_text() strips all tags from the document you are working with
     and returns a Unicode string containing the text only'''
    print(name.getText())