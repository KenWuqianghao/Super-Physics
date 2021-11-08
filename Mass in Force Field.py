#!/usr/bin/env python
# coding: utf-8

# In[188]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[189]:


def force(x,y):
    return(- G * M * m * x / ((x ** 2 + y ** 2) ** 1.5))


# In[190]:


def position(a, v, y):
    return(0.5 * a * delta_t ** 2 + v * delta_t + y)


# In[191]:


def velocity(a, v):
    return(a * delta_t + v)


# In[192]:


def acc(f):
    return(f/M)


# In[193]:


t = np.linspace(0,10,1000)
G = 60
M = 10
m = 1
delta_t = 0.01

x = [10]
y = [0]
f_x = [force(x[0], y[0])]
f_y = [force(y[0],x[0])]
v_x = [0]
v_y = [3]
a_x = [f_x[0] / m]
a_y = [f_y[0] / m]


# In[194]:


for i in range (1,len(t)):
    x.append(position(a_x[i - 1], v_x[i - 1], x[i - 1]))
    y.append(position(a_y[i - 1], v_y[i - 1], y[i - 1]))

    v_y.append(velocity(a_y[i - 1], v_y[i - 1]))
    v_x.append(velocity(a_x[i - 1], v_x[i - 1]))

    f_y.append(force(y[i], x[i]))
    a_y.append(acc(f_y[i]))
    
    f_x.append(force(x[i], y[i]))
    a_x.append(acc(f_x[i]))


# In[195]:


i = 3
print(x[i])
print(y[i])
print(v_x[i])
print(v_y[i])
print(f_x[i])
print(f_y[i])
print(a_x[i])
print(a_y[i])


# In[196]:


plt.scatter(x,y)
plt.show()

