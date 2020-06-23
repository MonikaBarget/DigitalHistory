# Generate word cloud from several WORD documents using tri-lingual stopwords

from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import os
import os.path
from os.path import dirname, join
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# nltk.download('punkt')

# read WORD files from directory and convert them to plain text

in_directory=("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\FBIIIProtokolle_TXT")
fnames=(os.listdir(in_directory))

with open('C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\FBIIIProtokolle_TXT\\Alle_Protokolle.txt', 'w', encoding='utf-8') as infile:
    for fname in fnames:
        filename=os.path.join(in_directory, fname)
        with open(filename) as file:
            for line in file:
                infile.write(line)
                                
# define stopwords and convert them to string

stopwords_multiling=stopwords.words('en_fr_de')
data4=set(stopwords_multiling)
print(type(data4))
print(data4)

# read and pre-process data
  
with open('C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\FBIIIProtokolle_TXT\\Alle_Protokolle.txt', 'r', encoding='utf-8', errors='ignore') as f: # open file
    data1=f.read() # read content of file as string
  # print(data1)
    data2=data1.translate(str.maketrans('', '', string.punctuation)).lower() # remove punctuation
    data3=" ".join(data2.split()) # remove additional whitespace from text

# define word cloud layout
  
wordcloud = WordCloud(width = 1000, height = 1000, 
                background_color ='white', 
                max_words=50,      
                stopwords=data4, 
                min_font_size = 12).generate(data3) 
  
# plot the WordCloud image   

plt.figure(figsize = (10, 10), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 10) 
  
plt.show() 
