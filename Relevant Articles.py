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

# def relavent():
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
m2.append(k)
  
h =[]
m =[]
# os.chdir('articles') 
my_files = glob.glob('*.txt')
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
    
    
   