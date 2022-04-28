#!/usr/bin/env python
# coding: utf-8

# In[7]:


def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,2,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) #Fals
all_unique(y) #True


# In[ ]:




