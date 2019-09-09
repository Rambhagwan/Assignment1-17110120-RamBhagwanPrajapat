#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import pandas as pd
import nltk
from nltk.tokenize import TweetTokenizer


# In[14]:


#que 1
datafile = pd.read_csv("tweets-dataset.csv")
total_token = list()
total_type = set()
tk = TweetTokenizer()
for sentence in datafile['Sentence']:
    word_list = tk.tokenize(sentence)
    for ele in range(len(word_list)):
        word = word_list[ele]
        total_token.append(word)
        total_type.add(word)


# In[15]:


print("token :",len(total_token))
print("type :",len(total_type))
ttr = len(total_type)/len(total_token)
print("ttr : ",ttr,sep="")


# In[23]:


#que 3
import matplotlib.pyplot as plt
plt.title("Heap's law")
ls = list()
sett = set()
lss = list()
for i in range(len(total_token)): #total token from above que 1 code
    sett.add(total_token[i])
    ls.append(i)
    lss.append(len(sett))
plt.xlabel("Token : N")
plt.ylabel("Vocabulary size : ")
plt.plot(ls,lss)
print("#plot of Heap's law")


# In[31]:


#que 2
nltk.download('wordnet')
from nltk.corpus import wordnet
import random
vocab = list(sett)
x_axis = []
y_axis = []
for i in range(len(total_token)):
    rand_word = random.randint(0,len(vocab)-1)
    synonyms = list()
    for j in wordnet.synsets(vocab[rand_word]):
        for item in j.lemmas():
            if vocab[rand_word]==item.name():
                synonyms.append(item.name())
    if len(synonyms)>=6 and len(synonyms)<=60:
        x_axis.append(len(synonyms))
        y_axis.append(len(vocab[rand_word]))
    #taking 25 random points
    if len(x_axis)>=25:
        break
plt.scatter(x_axis,y_axis)
plt.title("zipf's law")
plt.xlabel("Number of meanings")
plt.ylabel("Length of token")
plt.show()


# In[ ]:




