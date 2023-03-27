
#Start with try because is possible the go down so yo need to consider
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
except URLError as e:
    print('The server could not be foound!')
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement
    print('It Worked')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)

'''
This checking and handling of every error does seem laborious at first, but it’s easy to
add a little reorganization to this code to make it less difficult to write (and, more
important, much less difficult to read). This code, for example, is our same scraper
written in a slightly different way:
'''
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
 print('Title could not be found')
else:
 print(title)
'''
'''In this example, you’re creating a function getTitle, which returns either the title of
the page, or a None object if there was a problem retrieving it. Inside getTitle, you
check for an HTTPError, as in the previous example, and encapsulate two of the Beau‐
tifulSoup lines inside one try statement. An AttributeError might be thrown from
either of these lines (if the server did not exist, html would be a None object, and
html.read() would throw an AttributeError). You could, in fact, encompass as
many lines as you want inside one try statement, or call another function entirely,
which can throw an AttributeError at any point.'''
'''÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷'''