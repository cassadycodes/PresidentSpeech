"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
Webscraper to collect urls for corpus of Presidential Speeches & Remarks
"""
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from time import sleep
from random import randint

## Navigate White House Briefing Room
# first we'll make a list of links to each remarks page and exclude irrelevant results
urls = [] # url collection list
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
for n in range(1,9): # currently eight pages of speeches and remarks
    page = requests.get("https://www.whitehouse.gov/briefing-room/speeches-remarks/page/" + str(n),headers=headers) # insert page number n to url
    soup = BeautifulSoup(page.text,'html.parser')
    # get link iff title contains "by President" (exclude e.g. remarks by VP)
    links = soup.find_all('a', class_='news-item__title') # note: prefer to exclude here but can't figure out
    for link in links: # extracting hrefs
        if "by President" in link.text: # exclude VP remarks etc.
            urls.append(link.get('href')) # add link to url list
    sleep(randint(2,10)) # politely limit our request rate as we navigate to the next page
# urls list should now contain all of the links to Biden's speeches and remarks!

# save urls to .txt file for source list
with open('urls.txt','w+') as file:
    for url in urls:
        file.write('%s\n' %url)
file.close()
print("Links added to urls.txt")

