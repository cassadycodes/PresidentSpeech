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

######################################################################
## Modification of get_urls.py to get Trump White House urls from
## https://trumpwhitehouse.archives.gov/remarks/page/
## need page 29-37 for remarks during coronavirus beginning 2 March 2020
######################################################################

urls = [] # url collection list
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
for n in range(29,38): # pages 29-37
    page = requests.get("https://trumpwhitehouse.archives.gov/remarks/page/" + str(n),headers=headers) # insert page number n to url
    soup = BeautifulSoup(page.text,'html.parser')
    # get link iff title contains "by President" (exclude e.g. remarks by VP)
    ## adjustment: title class on <h2> tag not <a> tag
    titles = soup.find_all('h2', class_='briefing-statement__title') 
    for title in titles: # extracting hrefs
        if "by President" in title.findChild().text: # exclude VP remarks etc.
            urls.append(title.findChild().get('href')) # add link to url list
    sleep(randint(2,10)) # politely limit our request rate as we navigate to the next page
# urls list should now contain all of the links to Biden's speeches and remarks!

# save urls to .txt file for source list
with open('trump_urls.txt','w+') as file:
    for url in urls:
        file.write('%s\n' %url)
file.close()
print("Links added to trump_urls.txt")

