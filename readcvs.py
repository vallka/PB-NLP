# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:46:40 2018

@author: vkulikov
"""


import glob
import os
import spacy
nlp_en = spacy.load('en_core_web_sm')

dir1='cvdata\\1'

os.getcwd()
os.path.join(os.getcwd(), dir1, "*.txt")

file_list = glob.glob(os.path.join(os.getcwd(), dir1, "*.txt"))

corpus = []
corpus2 = []

for file_path in file_list:
    with open(file_path, encoding='utf-8', errors='ignore') as f_input:
        corpus.append(f_input.read())


print(len(corpus))

for i in range(0,len(corpus)):
    cv1 = corpus[i]
    cv1a = cv1.encode('ascii', 'ignore').decode("utf-8")
    corpus2.append(nlp_en(cv1a))
    print (i)
    


print(len(corpus2))


for i in range(0,len(corpus)):
    for j in range(i+1,len(corpus)):
#        print (i,j,doc[i].similarity(doc[j]))     
        print (i)
        print (j)
        print (corpus2[i].similarity(corpus2[j]))

#cv1a = cv1.translate(translator)
#cv1a
#cv1a

#import nltk
#nltk.download('stopwords')
  
#from nltk.corpus import stopwords
#stop_en = stopwords.words("english")
#stop_en



