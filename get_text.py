"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
Webscraper to collect raw text for corpus of Presidential Speeches & Remarks
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

## Data Collection
# now we go to each link and gather the raw text content
counter = 0 # count links
with open('urls.txt') as urls:
    file = open("biden.txt", "w")
    for url in urls: # access each link
        counter += 1 # increment link counter
        print("Current Page",counter,"of 72 ",url) # helper print statement
        page = requests.get(url.strip()) # must strip newline char from end of url
        soup = BeautifulSoup(page.text,'html.parser') # create soup object
        # luckily <p> tags are only inside the main content section! very helpful :)
        for p in soup.find_all('p'): # find all paragraphs
            line = p.get_text() # get text (exclude HTML tags)
            file.writelines(line+" ") # write each paragraph to file, add whitespace
        sleep(randint(2,10)) # limit requests
    file.close()
    print("Done! Text saved to biden.txt")
file.close()

### TODO Cleaning
## Need to exclude: - interviewers Q - timestamp - location - notes such as (The executive order is signed.)
## Have to do this BEFORE tokenization