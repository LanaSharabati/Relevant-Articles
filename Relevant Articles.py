# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:18:15 2022

@author: Asus
"""
import glob
import os

def histogram(word_list):
    
   word_histogram = {
   }
   for word in word_list:
       if word not in word_histogram.keys():
           word_histogram[word] = 1
       else:
           word_histogram[word] = word_histogram[word] + 1
   word_histogram.pop("")
   return(word_histogram)

def list_(input_text):
    irrelevant_words = {".", "," , "\n", 'the', " a ", " and ",
    " is ", " was ", " he ", " at ", " to ", " for ", " can ",
    "of","that","in","by","on","said","his","will","are",
    '"'}
    for iw in irrelevant_words:
        input_text = input_text.replace(iw, " ")
        word_list = input_text.split(" ")
    return word_list

def keywords(my_dict):####
    x=list(my_dict.values())
    x.sort(reverse=True)
    x=x[:2]
    y = []
    for i in x:
        for j in my_dict.keys():
            if(my_dict[j]==i):
                y.append(str(j))
    return(y)

def relavent(keyword1,keyword2,file):
    c=0
    for i in range(len(keyword1)):
        for j in range(len(keyword2)):
            if keyword1[i] == keyword2[j]:
                c = c+1
    return [c,file]
        
        
    
    
os.chdir('articles')    
"'Article0.txt'"    
h2 =[]
m2 =[]
file_read = input("enter file name") 
# os.chdir('articles')

file = open(file_read)
input_text = file.read()
word_list = list_(input_text)
a = histogram(word_list) 
h2.append(a)
k= keywords(a)


  
h =[]
m =[]
r=[]
# os.chdir('articles') 
my_files = glob.glob('*.txt')

my_files.remove(file_read)
print(my_files)
for i in range(len(my_files)):
    if my_files[i] != file_read:
        file = open(my_files[i])
        input_text2 = file.read()
        word_list = list_(input_text2)
        a = histogram(word_list) 
        h.append(a)
        k= keywords(a)
        m.append(k)
    

for i in range(len(m)):
    re = relavent(k,m[i],my_files[i])
    r.append(re)
    
q=[]
maxi = max(r)
for i in range(len(r)):
    if maxi[0] == r[i][0]:
        q.append(r[i][1])   
    
print("articles with the most intersection",q)   