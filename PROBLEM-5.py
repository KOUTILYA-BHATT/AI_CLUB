#!/usr/bin/env python
# coding: utf-8

# In[10]:


import math
class Practice:
    def equation(self):
        y=input("Enter the value of D\t").split(",")
        d=[]
        for x in y:
            d.append(int(x))
    
        Q=[]
        c=50
        h=30
        for no in d:
            q=int(math.sqrt((2*c*no)/h))
            Q.append(str(q))
        print(','.join(Q))
        
        
    def array(self):
        row_num = int(input("Input number of rows: "))
        col_num = int(input("Input number of columns: "))
        multi_list = [[row*col for col in range(col_num)] for row in range(row_num)]

        print(multi_list)
        
    def sorting(self):
        mylist = input("Enter any list seperated by commas ")
        final= mylist.split(",")
        final.sort()
        print(','.join(final))
        
    def freq(self):
        string = input("Enter any string ")
        mylist=string.split(' ')
        mylist.sort()
        dictionary={}
        for words in mylist:
            counts=mylist.count(words)
            dictionary.update( {words:counts} )
    
        print(dictionary)
    
prac=Practice()
prac.equation()
prac.array()
prac.freq()
prac.sorting()


# In[ ]:




