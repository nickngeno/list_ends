#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""

def listends(object):
    return a[0],a[-1]
    
a=[5, 10, 15, 20, 25]   
listends(a)


# In[49]:


import random
rrand=[random.randrange(1,9,1)for i in range(7)]
# print (rrand)
# rrand=[i for i in rrand]
def make_alist(object):
    return rrand[0],rrand[-1]
make_alist(rrand)

