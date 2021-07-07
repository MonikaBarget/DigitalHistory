# Book index with NLTK frequency counter

# based on a tutorial by by Abder-Rahman Ali, 12 Dec 2016

# https://code.tutsplus.com/tutorials/preparing-a-book-index-using-python--cms-27556

# use cases: book index for publication, tagging, ontologies

import nltk, collections
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv

# define stop words

my_stopwords=stopwords.words('en_fr_de') # call custom NLTK stopword list from local nltk-data folder
my_stopwords.extend(['?', '&', '!', '’', ':', '..']) # expand stopword list if necessary

# count frequency of individual words excluding stop words
 
frequencies=collections.Counter()
with open("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\BRILL\\INDEX\\INDEX.txt", encoding="utf-8") as book:
    read_book=book.read()
words=nltk.word_tokenize(read_book) 

filtered_text = [w for w in words if not w.lower() in my_stopwords]
filtered_text = sorted(list(dict.fromkeys(filtered_text)))

print(filtered_text)

for f in filtered_text:
    frequencies[f] += 1
     
print(frequencies) 
print(type(frequencies))
most_frequent={k:v for (k,v) in frequencies.items() if 25 > v > 3} # dict comprehension
print(most_frequent)

# write tokens and frequencies to table

with open("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\BRILL\\INDEX\\INDEX_freq.csv", "w", encoding="utf-8") as freq_csv:    
    write=csv.writer(freq_csv)
    for key, value in frequencies.items():
        write.writerow([key, value])
        
# count frequency of n-grams

# Combinations of words that often co-occur are called collocations.
# An example of collocations is bigrams, that is a list of word pairs. 
# Similar to that is trigrams (a combination of three words), and so forth (i.e. n-grams).

# extracting n-grams

bigram = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words)

# ignore all bigrams that occur at least "n" times

finder.apply_freq_filter(3) 

# print 30 most frequent bigrams

print (finder.nbest(bigram.pmi, 30)) 

# find the location of word or phrase in text

print (read_book.index('newspaper')) 

# find the location of word or phrase in text

print (read_book.index('journal')) 
