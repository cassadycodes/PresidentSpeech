import nltk
import string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


president = "trump"

# load text and separate tokens
file = open(f"{president}_cleaned.txt", "rb")
text = file.read().decode(errors='replace')
file.close()

# load stopwords list
stopwords = nltk.corpus.stopwords.words("english")
# NLTK's default stopwords list is not comprehensive so we will add some more
add_stops = ['a.m.','p.m.','mr.','mrs.','ms.','dr.',"'s","'re","'ve", "yeah", "thank", "please", "god", "bless"]
for stop in add_stops:
    stopwords.append(stop)

# tokenization
# [made previously for HarvardX CS50-AI "Questions" project, with small changes]
tokens = nltk.word_tokenize(text)
# eliminate punctuation and stopwords
tokens = [word.lower() for word in tokens if word.lower() not in stopwords and word not in string.punctuation and any(c.isalpha() for c in word)] 
# any(c.isalpha() for c in word) says "if any character in word is in the alphabet"
# which eliminates extraneous punctuation "===" but keeps words like "text-to-speech" 


# Thank you to Darius Fuller for this guide on creating visuals https://dariuslfuller.medium.com/creating-visuals-with-nltks-freqdist-ac4e667e49f3

## Generate bigrams
ngrams_list = nltk.trigrams(tokens) # toggle bigrams / trigrams

## Creating FreqDist
ngrams_freq = nltk.FreqDist(ngrams_list).most_common(20)

ngram_fd = dict(ngrams_freq)


## Sort values by highest frequency
ngram_sorted = {k:v for k,v in sorted(ngram_fd.items(), key=lambda item:item[1])}

## Join bigram tokens with '_' + maintain sorting
ngram_joined = {'_'.join(k):v for k,v in sorted(ngram_fd.items(), key=lambda item:item[1])}

## Convert to Pandas series for easy plotting
ngram_freqdist = pd.Series(ngram_joined)

## Setting figure & ax for plots
fig, ax = plt.subplots(figsize=(10,10))

## Setting plot to horizontal for easy viewing + setting title + display  
bar_plot = sns.barplot(x=ngram_freqdist.values, y=ngram_freqdist.index, orient='h', ax=ax)
plt.title('Frequency Distribution')
plt.show();
