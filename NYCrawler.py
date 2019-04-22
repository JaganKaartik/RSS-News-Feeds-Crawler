#NewYork Times News RSS/XML Crawler 

from bs4 import BeautifulSoup
import requests
import time
import sys
start = time.time()

text = input("Enter search query : ")
#text = sys.argv[1]
print(text)
htmlurl = 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/'+text+'/rss.xml'
url = requests.get(htmlurl)
soup = BeautifulSoup(url.text,'xml')

titles = soup.findAll('title')
titles.pop(0)

links = soup.findAll('link')
links.pop(0)

pubDates = soup.findAll('pubDate')
pubDates.pop(0)

author = soup.findAll('author')

descriptions = soup.findAll('description')
descriptions.pop(0)

#Dictionary to hold crawled information

NYTfeedDict = {}
te = []

for i in titles:
	te.append(i.get_text())
	NYTfeedDict['title'] = te
te = []
for i in links:
	te.append(i.get_text())
	NYTfeedDict['link'] = te
te = []
for i in pubDates:
	te.append(i.get_text())
	NYTfeedDict['pubdate'] = te
te = []
for i in descriptions:
	te.append(i.get_text())
	NYTfeedDict['description'] = te
te = []
for i in author:
	string = i.get_text();
	string = string[3:]
	te.append(string)
	NYTfeedDict['author'] = te

#Output Verification
print(NYTfeedDict['title'][0])
print(NYTfeedDict['link'][0])	
print(NYTfeedDict['pubdate'][0])
print(NYTfeedDict['description'][0])
print(NYTfeedDict['author'][0])


end = time.time()
print("Execution Time : ",end - start)
