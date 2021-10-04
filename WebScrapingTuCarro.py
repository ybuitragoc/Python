#!/usr/bin/env python
# coding: utf-8

# In[38]:


#poder leer la pagina
import urllib.request
datos = urllib.request.urlopen('https://carros.tucarro.com.co/usados').read().decode()


# In[ ]:





# In[26]:


import sys
get_ipython().system('{sys.executable} -m pip install beautifulsoup4')


# In[44]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(datos)
tags = soup('a')
#spans = soup.findAll('span')
spans = soup.findAll('span', attrs = {'class' : 'price-tag-fraction'}) # or span by class name
lis = soup.findAll('li', attrs = {'class' : 'ui-search-card-attributes__attribute'}) # or span by class name


for span in spans:
    print (span.text)
for li in lis:
    print (li.text)

   


# In[ ]:




