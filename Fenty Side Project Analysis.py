#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import collections
import matplotlib.cm as cm
from matplotlib import rcParams
import itertools


# In[20]:


df = pd.read_csv('Fenty_Cheek.csv')


# In[21]:


df


# In[46]:


all_materials = ''.join(df['Ingredients'].str.lower())


# In[47]:


all_materials


# In[24]:


ingr = df.Ingredients.apply(lambda x: pd.Series(str(x).split(",")))


# In[25]:


stopwords = set(STOPWORDS)

wordcloud = WordCloud(width = 900, height = 900,
                      stopwords = stopwords, min_font_size = 30).generate(all_materials)
plt.figure(figsize = (200, 200), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Fenty Beuaty Face Products")
plt.show()


# In[59]:


# Identify the top word in the ingredients 
words = [word for word in all_materials.split() if word not in stopwords]
counted_words = collections.Counter(words)

ingredient = []
counts = []
for materials, count in counted_words.most_common(10):
    ingredient.append(materials)
    counts.append(count)


# In[61]:


# Create a rainbow color 
colors = cm.rainbow(np.linspace(0, 1, 10))
rcParams['figure.figsize'] = 20, 10

plt.title('Top words in Fenty Face Products vs their counts')
plt.xlabel('Count')
plt.ylabel('Ingredients')
plt.barh(ingredient, counts, color=colors)
plt.show()


# In[ ]:




