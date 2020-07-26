# script for topic modelling based on Scikit Learn and NLTK stopword list
# adapted from DARIAH-DE tutorial

# import necessary modules

import os
import numpy as np
import sklearn.feature_extraction.text as text # submodule gathers utilities to build feature vectors from text documents
from sklearn import decomposition
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# call custom NLTK stopword list, stored locally in nltk-data folder

my_stopwords=stopwords.words('en_fr_de')

# extend list if necessary

my_stopwords.extend(['@', 'forschungsbereich', 'frage']) 
print(my_stopwords)

# read .txt files to be analysed from directory

CORPUS_PATH=("C:\\Users\\mobarget\\Google Drive\\ACADEMIA\\FBIII_OCRTexts")

filenames=sorted([os.path.join(CORPUS_PATH, filename) for filename in os.listdir(CORPUS_PATH)])
print(len(filenames)) # count files in corpus
print(filenames[:10]) # print names of 1st ten files in corpus
            
# apply stopword list and vectorise data

vectorizer=text.CountVectorizer(input='filename', stop_words=my_stopwords, min_df=0.1) 

# min_df: float in range [0.0, 1.0] or int, default=1
# When building the vocabulary ignore terms that have a document frequency 
# strictly lower than the given threshold. This value is also called cut-off
# in the literature. If float, the parameter represents a proportion of documents,
# integer absolute counts. This parameter is ignored if vocabulary is not "None".

# define document term matrix
dtm=vectorizer.fit_transform(filenames).toarray() 

vocab=np.array(vectorizer.get_feature_names())
print(dtm.shape)

# vocabulary size of corpus
print(len(vocab))

# generate topics and select representative words
num_topics=6 # no. of topics
num_top_words=30 # no. of words per topic to be displayed

clf=decomposition.NMF(n_components=num_topics, random_state=1)

# random_state : int
# RandomState instance or None, optional (default=None)
# If int, random_state is the seed used by the random number generator; 
# If RandomState instance, random_state is the random number generator; 
# If None, the random number generator is the RandomState instance used by np.random.

doctopic=clf.fit_transform(dtm) 

topic_words=[] # list of most prominent words associated with topics
for topic in clf.components_: 
   
    word_idx=np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i] for i in word_idx])
    
# output results
    print(topic_words) 
    
    
doctopic=doctopic/np.sum(doctopic,axis=1,keepdims=True)
    
# names of texts associated with each topic (according to topic shares in MALLET)  
text_names=[]   
for fn in filenames:
    
    basename=os.path.basename(fn)
    name, ext=os.path.splitext(basename)
    name=name.rstrip('0123456789')
    text_names.append(name)

text_names=np.asarray(text_names) # turn into array to use NumPy function

# list all file names in corpus
print(text_names) 
        
doctopic_orig=doctopic.copy()
        
print(doctopic_orig)
        
num_groups=len(set(text_names))
print(num_groups) 
        
doctopic_grouped=np.zeros((num_groups, num_topics)) 
        
for i, name in enumerate(sorted(set(text_names))):
    doctopic_grouped[i,:]=np.mean(doctopic[text_names==name,:],axis=0)
            
doctopic=doctopic_grouped
            
texts=sorted(set(text_names))
           
# show top three topics per text in corpus

print("Top NMF topics in ...")
            
for i in range(len(doctopic)):
# defines number of topics per text
    top_topics=np.argsort(doctopic[i,:])[::-1][0:3] 
    top_topics_str=' '.join(str(t)for t in top_topics) 
    print("{}:{}".format(texts[i],top_topics_str)) 
    
# show top words

for t in range(len(topic_words)):

# defines max. number of words displayed in output
    print("Topic{}:{}".format(t, ' '.join(topic_words[t][:31]))) 

# Print "done" to indicate successful completion

print("done")
