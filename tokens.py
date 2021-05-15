"""
Cassady Shoaff | Montclair State University | APLN580 Corpus Linguistics | Spring 2021
NLTK tokenization and keyword extraction
"""
import nltk
# nltk.download() # only need this if it's first time using nltk
from nltk.corpus import stopwords
import string

president = "biden" # use lowercase
print("President",president.upper())

# load text and separate tokens
file = open(f"{president}_cleaned.txt", "rb")
text = file.read().decode(errors='replace')
file.close()

# load stopwords list
stopwords = nltk.corpus.stopwords.words("english")
# NLTK's default stopwords list is not comprehensive so we will add some more
add_stops = ['a.m.','p.m.','mr.','mrs.','ms.','dr.',"'s","'re","'ve"]
for stop in add_stops:
    stopwords.append(stop)

# tokenization
# [made previously for HarvardX CS50-AI "Questions" project, with small changes]
tokens = nltk.word_tokenize(text)
# eliminate punctuation and stopwords
tokens = [word.lower() for word in tokens if word.lower() not in stopwords and word not in string.punctuation and any(c.isalpha() for c in word)] 
# any(c.isalpha() for c in word) says "if any character in word is in the alphabet"
# which eliminates extraneous punctuation "===" but keeps words like "text-to-speech" 

total_tokens = len(tokens) # count total tokens
types = len(set(tokens)) # unique tokens

print("Types:",types,"Tokens: ",total_tokens)

# find the frequency
freq = nltk.FreqDist(tokens)
bi = nltk.bigrams(tokens)
#print(*map(' '.join, bi), sep=', ')

# readability 
letters = 0
words = 1
sentences = 0
for c in text:
    if c.isalpha() == True:
        letters += 1
    if c.isspace() == True:
        words += 1
    if c == "." or c == "!" or c == "?":
        sentences += 1

avgletters = letters / words * 100
avgsentences = sentences / words * 100
# Flesch-Kincaid formula
grade = int(round(0.0588 * avgletters - 0.296 * avgsentences - 15.8))

if grade > 15:
    print("Readability: Grade 16+")
elif grade < 1:
    print("Readability: Before Grade 1")
else:
    print("Readability: Grade ", grade)


# save data 
file = open(f"{president}_tokens.txt", "w", encoding="utf-8")
file.writelines("Tokens: " + str(total_tokens) + "\n")
file.writelines("Types: " + str(types) + "\n")
file.writelines("Readability: " + str(grade) + "\n")
for k,v in freq.items():
    file.writelines(str(k)+':'+str(v)+'\n')
file.close()


# plot the frequency
freq.plot(25, cumulative=False)