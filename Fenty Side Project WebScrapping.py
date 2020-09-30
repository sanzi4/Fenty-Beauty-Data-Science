#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import re
import requests
from bs4 import BeautifulSoup


# In[56]:


# Link to Fenty Beauty Cheek products 
link = requests.get("https://www.sephora.com/brand/fenty-beauty-rihanna/cheek-makeup")
#print(link.text)
#print(link.content)

# Convert this HTMl document to a BeautifulSoup Object
soup = BeautifulSoup(link.content, "html.parser")
#print(soup)
#print(soup.title.text)


# In[57]:


# Create a list with all the Fenty Beauty Blush products
a = soup.select('.css-pelz90')
Name = []
for i in a[0:]:
    Name.append(i.get_text())
print(Name)


# In[58]:


# Create a list of all the prices
prices = []
for i in soup.select('.css-0'):
    prices.append(i.text)
print(prices)


# In[67]:


# len(prices)
# prices.pop(0)
prices


# In[68]:


# Create a list to store all the ingredients 
materials = []
met = []
def get_ingredients(link, classes):
    webpage = requests.get(link)
    soups = BeautifulSoup(webpage.content, "html.parser")
    for i in soups.select(classes):
        met.append(i.text)
        materials.append(met[-1:])


# In[101]:


# For the first Fenty Product 
get_ingredients("https://www.sephora.com/product/fenty-beauty-rihanna-cheeks-out-freestyle-cream-blush-P19700127?skuId=2352730", ".css-pz80c5")


# In[104]:


# materials.pop(0)
materials


# In[105]:


# For the second Fenty Product 
get_ingredients("https://www.sephora.com/product/sun-stalk-r-instant-warmth-bronzer-P55978864?icid2=products%20grid:p55978864", ".css-pz80c5")
# materials.pop(0)
# materials


# In[109]:


materials


# In[110]:


# For the third Fenty products
get_ingredients("https://www.sephora.com/product/fenty-beauty-rihanna-cheeks-out-freestyle-cream-bronzer-P31870457?icid2=products%20grid:p31870457", ".css-pz80c5")


# In[113]:


# materials.pop(2)
materials


# In[114]:


# For the fourth product 
get_ingredients("https://www.sephora.com/product/killawatt-foil-freestyle-highlighter-palette-P37378513?icid2=products%20grid:p37378513", ".css-pz80c5")


# In[117]:


materials.pop(3)
# materials


# In[118]:


# The 5th product
get_ingredients("https://www.sephora.com/product/lil-bronze-duo-P442531?icid2=products%20grid:p442531", ".css-pz80c5")


# In[119]:


materials


# In[122]:


materials.pop(4)


# In[123]:


materials


# In[136]:


Name.pop(6)


# In[139]:


prices.pop(5)


# In[135]:


materials


# In[146]:


len(Name)


# In[142]:


len(prices)


# In[143]:


len(materials)


# In[144]:


Name


# In[145]:


Name.pop(5)


# In[149]:


# Display the data into a table 
dataframes = {"Name": Name, "Prices": prices, "Ingredients":materials}
Fenty_Cheek = pd.DataFrame.from_dict(dataframes)


# In[2]:


# Get all the desired information we want, Product Name, 
# Price, And Ingredients :

def get_information(link, productClass, priceClass, IngredientsClass):
    webpage = requests.get(link)
    soup = BeautifulSoup(link.content, "html.parser")
    productNames = []
    Prices = []
    Ingredients = []
    for i in soup.select(productClass):
        productNames.append(i.get_text)
    print("Product Names are: " + productNames)
    for j in soup.select(priceClass):
        Prices.append(j.get_text)
    print("Prices are: " + Prices)
    for z in soup.select(IngredientsClass):
        Ingredients.append(z.get_text)
    print("Materials are: " + Ingredients)


# Convert the table into a data tabke
def convert_to_Table(list1, Name1, list2, Name2, list3, 
                     Name3, list4, Name4):
    dataframes = {Name1: list1, Name2: list2, Name3: list3, Name4: list4}
    Fenty = pd.DataFrame.from_dict(dataframes)


# In[ ]:


# All the lipstick products 

