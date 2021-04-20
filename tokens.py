"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
NLTK tokenization and keyword extraction
"""
import nltk
nltk.download()
from ntlk.corpus import stopwords

# load text and separate tokens
file = open("biden_cleaned.txt")
text = file.read()
tokens = [t for t in text.split()]

# remove stopwords
stop = stopwords.words('english')
for token in tokens:
    if token in stop:
        tokens.remove(token)

# find the frequency
freq = nltk.FreqDist(tokens)

for k,v in freq.items():
    print(str(key)+':'+str(val))
    
freq.plot(20, cumulative=False)