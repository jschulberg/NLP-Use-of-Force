#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import os
import pandas as pd
import functools


# ### Load in Data

# In[5]:


data_path = 'C:/Users/ftinelli/Documents/Python Scripts/NLS_Mentorship_Program/NLP-Use-of-Force/Data/Cleaned_Text'

# Creates a single dataframe with a policy for each row by city.
def bind_rows(dfs, ignore_index=True):
    return functools.reduce(lambda t,b: pd.concat([t,b], ignore_index=ignore_index), dfs)


header_list = ['Policy']

files = []
for i in os.listdir(data_path):
    txt = os.path.join(data_path, str(i))
    city = i.split('_')[0]
    if 'Extract' in txt:
        f = pd.read_csv(txt, names=header_list)
        f['City'] = city
        f = f[['City','Policy']]
        files.append(f)

df = bind_rows(files)


# In[22]:


df.head()


# In[7]:


len(df)


# ### Latent Dirichlet Allocation (LDA)

# #### Assumptions <br>
# Policies with similar topics use similar groups of words. <br>
# Latent topics can then be found by searching for groups of words that frequently occur together in policies across the corpus (collections of policies). <br>
# Policies are probablity distributions over latent topics. <br>
# Topics themselves are probability distributions over words. <br>

# In[44]:


# Perform some pre-processing.

# Count vectorization - counting the number of occurrences each words appears in a document.
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer


# In[45]:


# Initiate an instance of count vectorizer.
# max_df - gets rid of words with high frequency across the documents.
# min_df - get rid of words with don't meet minumum frequency.
cv = CountVectorizer(max_df=0.9, min_df=2)
tfidf= TfidfVectorizer(ngram_range=(1,3),max_df=0.9, min_df=0.01)


# In[46]:


# Fit transform to entire dataset.
# No train-test split as this is unsupervised learning.
dtm = cv.fit_transform(df['Policy']) # document term matrix.
dtm_ifidf = tfidf.fit_transform(df['Policy']) # document term matrix.


# In[12]:


dtm


# In[47]:


dtm_ifidf


# In[35]:


# Perform LDA.
from sklearn.decomposition import LatentDirichletAllocation,NMF


# In[28]:


# n_components - number of topics returned.
LDA = LatentDirichletAllocation(n_components=3,random_state=42)


# In[39]:


nmf = NMF(n_components=8,random_state=42)


# In[29]:


# Fit LDA to document term matrix.
LDA.fit(dtm)


# In[48]:


nmf.fit(dtm_ifidf)


# In[30]:


# Grab the vocabulary of words.
import random

random_word_id = random.randint(0,6924)

cv.get_feature_names()[random_word_id]


# In[31]:


# Grab the topics.

# Look at one topic first.
single_topic = LDA.components_[0]

# Sort words by their probability and get top 15.
# argsort() returns index from least to greatest.
single_topic.argsort()[-15:]

# Display top ten words.
top_fifteen_words = single_topic.argsort()[-15:]

for index in top_fifteen_words:
    print(cv.get_feature_names()[index])


# In[32]:


# Grab the highest probability words per topic.
for i,topic in enumerate(LDA.components_):
    print(f'The Top 15 Words for Topic #{i}')
    print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])
    print('\n')
    print('\n')


# In[50]:


# Grab the highest probability words per topic.
for i,topic in enumerate(nmf.components_):
    print(f'The Top 15 Words for Topic #{i}')
    print([tfidf.get_feature_names()[index] for index in topic.argsort()[-15:]])
    print('\n')
    print('\n')


# In[19]:


# Appends topics to policies.
topic_results = LDA.transform(dtm)

df['Topic'] = topic_results.argmax(axis=1)


# In[20]:


df


# In[ ]:




