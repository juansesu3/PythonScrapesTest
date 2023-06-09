import requests
from bs4 import BeautifulSoup

class Content:
	'''
	Common base for all articles/pages
	'''
	def __init__(self, topic, url, title, body):
		self.topic = topic
		self.title = title
		self.body = body
		self.url = url

	def print(self):
		'''

		Flexible printing function controls out
		'''
		print('New article found topic: {}'.format(self.topic))
		print('TITLE: {}'.format(self.title))
		print('BODY:\n{}'.format(self.body))
		print('URL: {}'.format(self.url))

class Website:
	'''
	Contains information about website structure
	'''
	def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
		self.name = name
		self.url = url
		self.searchUrl = searchUrl
		self.resultListing = resultListing
		self.resultUrl = resultUrl
		self.absoluteUrl = absoluteUrl
		self.titleTag = titleTag
		self.bodyTag = bodyTag

class Crawler:
	def getPage(self, url):
		try:
			req = requests.get(url)
			print(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(req.text, 'html.parser')
	def safeGet(self, pageObj, selector):
		chilObj = pageObj.select(selector)
		if chilObj is not None and len(chilObj) > 0:
			return chilObj[0].get_text()
		return ''
	def search(self, topic, site):
		'''
		Searches a given website for a given topic and records all pages found
		'''
		bs = self.getPage(site.searchUrl + topic)
		searchResults = bs.select(site.resultListing)
		for result in searchResults:
			url = result.select(site.resultUrl)[0].attrs['href']
			#Check to see whether it's a relative or and absolute URL
			if(site.absoluteUrl):
				bs = self.getPage(site.url + url)
			else:
				bs = self.getPage(site.url + url)
			if bs is None:
				print('Something was wrong with that page or URL. Skipping!')
				return
			title = self.safeGet(bs, site.titleTag)
			body = self.safeGet(bs, site.bodyTag)
			if title != '' and body != '':
				content = Content(topic, title, body, url)
				content.print()

crawler = Crawler()

siteData =[['O\'Reilly Media', 'http://oreilly.com', 'https://www.oreilly.com/search/?q=', '#main article', 'div.title-info > div > div > h1', True, 'h1', 'div.title-description.t-description.sbo-reader-content > div'],
	['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content', 'h3.search-result-title a', False, 'h1', 'article > div.ArticleBodyWrapper'],
	['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=', 'div.list-content article', 'h4.title a', False, 'h1','div.post-body']
	 ]
sites =[ ]
for row in siteData:
	sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7]))
topics = ['python', 'data+science']
for topic in topics:
	print(f'GETTING INFO ABOUT: ' + topic)
	for targerSite in sites:
		crawler.search(topic, targerSite)
