#Google News RSS/XML Crawler 

from bs4 import BeautifulSoup
import requests
import time
start = time.time()

text = input("Enter search query : ")
htmlurl = 'https://news.google.com/rss/search?q='+text
url = requests.get(htmlurl)
soup = BeautifulSoup(url.text,'xml')

titles = soup.findAll('title')
titles.pop(0)

links = soup.findAll('link')
links.pop(0)

pubDates = soup.findAll('pubDate')
pubDates.pop(0)

descriptions = soup.findAll('description')
descriptions.pop(0)

#Dictionary to hold crawled information

GfeedDict = {}
te = []

for i in titles:
	te.append(i.get_text())
	GfeedDict['title'] = te
te = []
for i in links:
	te.append(i.get_text())
	GfeedDict['link'] = te
te = []
for i in pubDates:
	te.append(i.get_text())
	GfeedDict['pubdate'] = te
te = []
for i in descriptions:
	string = i.get_text()
	string = string.split('<p>')[1]
	string = string[:-4]
	te.append(string+"Read More")
	GfeedDict['description'] = te

#Output Test
print(GfeedDict['title'][0])
print(GfeedDict['link'][0])	
print(GfeedDict['pubdate'][0])
print(GfeedDict['description'][0])

end = time.time()
print("Execution Time : ",end - start)
