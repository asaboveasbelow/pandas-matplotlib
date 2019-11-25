#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import pandas as pd
import matplotlib as plt
from matplotlib import pyplot as plt


# In[47]:


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #age


# In[48]:


dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] # salary


# In[49]:


plt.plot(ages_x, dev_y, label = 'All Devs')
plt.show()


# In[51]:


plt.style.use('fivethirtyeight')



plt.plot(ages_x,py_dev_y, color ='#5a7d9a',linewidth = 3, marker ='o', label = 'Python')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y, color ='#adad3b',linewidth = 3, label ='Javascript')


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


plt.plot(ages_x, dev_y, color ='#444444', linewidth = 3, linestyle='--', marker='.', label = 'All Devs')

plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary in (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()


# In[52]:


plt.style.use('ggplot')


plt.plot(ages_x,py_dev_y, color ='#5a7d9a',linewidth = 3, marker ='o', label = 'Python')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y, color ='#adad3b',linewidth = 3, label ='Javascript')


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


plt.plot(ages_x, dev_y, color ='#444444', linewidth = 3, linestyle='--', marker='.', label = 'All Devs')

plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary in (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()


# In[58]:


#plt.xkcd()


plt.plot(ages_x,py_dev_y, color ='#5a7d9a',linewidth = 3, marker ='o', label = 'Python')


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x,js_dev_y, color ='#adad3b',linewidth = 3, label ='Javascript')


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


plt.plot(ages_x, dev_y, color ='#444444', linewidth = 3, linestyle='--', marker='.', label = 'All Devs')

plt.title('Median salary (USD) by age')
plt.xlabel('Ages')
plt.ylabel('Median Salary in (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

#plt.savefig('plt.png')

plt.show()


# In[59]:


fig_1 = plt.figure(1, figsize=(6.4, 4.8))

chart_1 = fig_1.add_subplot(121)
chart_2 = fig_1.add_subplot(122)


# In[60]:


fig_1 = plt.figure(1, figsize=(20, 4.8))

chart_1 = fig_1.add_subplot(121)
chart_2 = fig_1.add_subplot(122)

