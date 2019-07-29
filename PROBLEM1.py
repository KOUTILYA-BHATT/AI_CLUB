#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROBLEM 1
import math
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


# In[ ]:




