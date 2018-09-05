# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:46:40 2018

@author: vkulikov
"""


import glob
import os
import spacy
nlp_en = spacy.load('en_core_web_sm')

dir1='cvdata\\jobs'
dir2='cvdata\\1'

os.getcwd()

file_list = glob.glob(os.path.join(os.getcwd(), dir1, "*.txt"))

corpus = []

for file_path in file_list:
    with open(file_path, encoding='utf-8', errors='ignore') as f_input:
        corpus.append(f_input.read())

print(len(corpus))


jobs=[]

for i in range(0,len(corpus)):
    cv1 = corpus[i]
    cv1a = cv1.encode('ascii', 'ignore').decode("utf-8")
    jobs.append(nlp_en(cv1a))
    print (i)
    

print ('jobs loded',len(jobs))



os.getcwd()

file_list2 = glob.glob(os.path.join(os.getcwd(), dir2, "*.txt"))

corpus = []

for file_path in file_list2:
    with open(file_path, encoding='utf-8', errors='ignore') as f_input:
        corpus.append(f_input.read())

print(len(corpus))


cands=[]

for i in range(0,len(corpus)):
    cv1 = corpus[i]
    cv1a = cv1.encode('ascii', 'ignore').decode("utf-8")
    cands.append(nlp_en(cv1a))
    print (i)
    

print ('jobs loded',len(cands))


best_cands=[0] * len(jobs)
best_cands_name=[0]*len(jobs)

for i in range(0,len(jobs)):
    best_cands[i] = 0
    for j in range(i+1,len(cands)):
#        print (i,j,doc[i].similarity(doc[j]))     
        print (i,file_list[i])
        print (j,file_list2[j])
        rank=jobs[i].similarity(cands[j])
        print (rank)
        if rank>best_cands[i]:
            best_cands[i]=rank
            best_cands_name[i]=file_list2[j]
            
            


print(best_cands)
print(best_cands_name)


