#!/usr/bin/env python
# coding: utf-8

# In[3]:


# PROBLEM 2
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[row*col for col in range(col_num)] for row in range(row_num)]

print(multi_list)


# In[ ]:




