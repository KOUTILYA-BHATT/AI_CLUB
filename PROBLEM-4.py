#!/usr/bin/env python
# coding: utf-8

# In[6]:


string = input("Enter any string ")
mylist=string.split(' ')
mylist.sort()
dictionary={}

for words in mylist:
    counts=mylist.count(words)
    dictionary.update( {words:counts} )
    
print(dictionary)


# In[ ]:




