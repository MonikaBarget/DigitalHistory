# Generate word cloud from text in English, French and German

from wordcloud import WordCloud # this is the package for generating the actual word cloud
import matplotlib.pyplot as plt # this package is needed for plotting the graph
import string # this package may be used for pre-processing
import nltk # this is Python's NLP library and is only needed if the text needs pre-processing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')

infile=("C:\\Users\\yourname\\yourpath\\yourfile.txt")  

# define stopwords and convert them to string

stopwords_multiling=stopwords.words('en_fr_de')
data4=set(stopwords_multiling)
print(type(data4))

# read and pre-process data
  
with open(infile, 'r', encoding='utf-8') as f: # open file
    data1=f.read() # read content of file as string
    data2=data1.translate(str.maketrans('', '', string.punctuation)).lower() # remove punctuation
    data3=" ".join(data2.split()) # remove additional whitespace from text

# define word cloud layout
  
wordcloud = WordCloud(width = 1000, height = 1000, 
                background_color ='white', 
                max_words=300,      
                stopwords=data4, 
                min_font_size = 12).generate(data3) 
  
# plot the WordCloud image   

plt.figure(figsize = (10, 10), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 10) 
  
plt.show() 
