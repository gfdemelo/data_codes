
# coding: utf-8

# In[1]:


a=[1,2,3]


# In[2]:


for item in a:
    print(item)


# Gabriel Fernando de Melo

# In[6]:


n=15
sum_of_squares = n * (n+1) * (2*n+1) // 6
print('1**2 + 2**2 + ... + {}**2 = {}'.format(n,
sum_of_squares))


# In[7]:


get_ipython().run_line_magic('pylab', 'inline')


# In[8]:


get_ipython().run_line_magic('pylab', 'inline --no-import-all')


# In[9]:


a=[1,2,3,4,5,6,7]
hist(a, 20, normed=True)


# > "Climb if you will, but remember that
# courage and strength are nought without
# prudence, and that a momentary negligence
# may destroy the happiness of a lifetime.
# Do nothing in haste; look well to each
# step; and from the beginning think what
# may be the end." - Edward Whymper

# n = 57
# while n != 1:
# if n % 2:
# n = 3*n + 1
# else:
# n //= 2

# In[11]:


ipython nbconvert --to latex <notebook.ipynb> --post pdf

