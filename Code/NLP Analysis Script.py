# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:57:08 2020

@author: jschulberg
"""

######################################
###        Import packages         ###
######################################
import os # Helps work with directories
import nltk # Helps with NLP work
from nltk.corpus import stopwords # Get our stop words
from collections import Counter # Helps with word counts
import re # Work with regular expressions
import matplotlib.pyplot as plt # Viz package
import numpy as np # numpy is used for deeper data analysis in python
import pandas as pd # Used for data analysis
import collections # Used for iterating on various datasets



######################################
###           Read in Data         ###
######################################
# Change the working directory
path = r'C:\Users\jschulberg\Documents\Learning\NLP\NLS Mentorship Program\NLP-Use-of-Force\Data\Cleaned_Text'
os.chdir(path)
os.getcwd()

# First find the names of the files we have
all_files = os.listdir()

# Initialize an empty list to hold all of our text
all_text = []

# Now read in all the files using a for loop. We have a lot!
for file in all_files:
    with open(os.path.join(path, file), 'rb') as f:
        # We have to decode the file so it doesn't accidentally get read in
        # as bytes
        text = f.read().decode('UTF-8')
        all_text.append(text)

# Let's take a peek into our dataset
print(all_text[0:100])

type(all_text) # Our data is in list format

# Our list is pretty long. Let's see if we can get everything into the
# list as one object. 
text_concat = ' '.join(policy for policy in all_text)


######################################
###     Text Pre-processing        ###
######################################
# In this section, we work on processing
# the text so it's ready for further analysis.
# This includes, but is not limited to:
#   1. Tokenizing text
#   2. Removing numbers
#   3. Fixing up words with inadvertent spaces
#   4. Removing insignificant (stop) words
#   5. Getting rid of contractions
#   6. Misc. text cleaning


# Make all the text lowercase
text_lower = text_concat.lower()

# Remove numbers
text_chars = re.sub(r"[0-9]", "", text_lower)

# Remove punctuation
text_chars = re.sub(r'[^\w\s]', '', text_chars)

### Fix words that were read in improperly
# There are a few words that are being read in improperly due to
# the conversion from PDF to TXT files. This can either look like
# an unneeded space separating a single word (i.e. de escalation)
# or the concatenation of two words that should be separated (i.e
# forcelethal). Because of this, we'll manually replace the words
# that appear most frequently in these forms.

# 'e scalation' --> 'escalation'
text_replaced = re.sub(r'e.scalation', 'escalation', text_chars)
# 'de escalation' --> 'deescalation'
text_replaced = re.sub(r'de.escalation', 'deescalation', text_chars)
# 'f orce' --> 'force'
# text_replaced = re.sub(r'\s[f]\s[orce]', 'force', text_replaced)
text_replaced = re.sub(r'f.orce', 'force', text_replaced)
# 'forcelethal' --> 'force lethal'
text_replaced = re.sub(r'\sforcelethal', 'force lethal', text_replaced)
# 'n eccessary' --> 'neccessary'
text_replaced = re.sub(r'n.ecessary', 'necessary', text_replaced)
# 'deadlyforce' --> 'deadly force'
text_replaced = re.sub(r'\sdeadlyforce', 'deadly force', text_replaced)
# 'excessiv e' --> 'excessive'
text_replaced = re.sub(r'excessiv.e', 'excessiv.e', text_replaced)
# 'm embers' --> 'members'
text_replaced = re.sub(r'm.embers', 'members', text_replaced)
# 'r eview' --> 'review'
text_replaced = re.sub(r'r.eview', 'review', text_replaced)
# 'p roportional' --> 'proportional'
text_replaced = re.sub(r'p.roportional', 'proportional', text_replaced)
# 'resi stance' --> 'resistance'
text_replaced = re.sub(r'resi.stance', 'resistance', text_replaced)
# 'r easonable' --> 'reasonable'
text_replaced = re.sub(r'resi.stance', 'resistance', text_replaced)
# 'd eadly' --> 'deadly'
text_replaced = re.sub(r'd.eadly', 'deadly', text_replaced)
# 'u se' --> 'use'
text_replaced = re.sub(r'u.se', 'use', text_replaced)
# 'g eneral' --> 'general'
text_replaced = re.sub(r'g.eneral', 'general', text_replaced)
# 'v olume' --> 'volume'
text_replaced = re.sub(r'v.olume', 'volume', text_replaced)
# 'f ebruary' --> 'february'
text_replaced = re.sub(r'f.ebruary', 'february', text_replaced)
# 'februar y' --> 'february'
text_replaced = re.sub(r'februar.y', 'february', text_replaced)
# 'p rocedures' --> 'procedures'
text_replaced = re.sub(r'p.rocedures', 'procedures', text_replaced)
# 'o perating' --> 'operating'
text_replaced = re.sub(r'o.perating', 'operating', text_replaced)
# 'o rder' --> 'order'
text_replaced = re.sub(r'o.rder', 'order', text_replaced)
# 'p olice' --> 'police'
text_replaced = re.sub(r'p.olice', 'police', text_replaced)
# 'd epartment' --> 'department'
text_replaced = re.sub(r'o.rder', 'order', text_replaced)
# 'b oard' --> 'board'
text_replaced = re.sub(r'b.oard', 'board', text_replaced)
# 't ucson' --> 'tucson'
text_replaced = re.sub(r't.ucson', 'tucson', text_replaced)





### Tokenize text
# Split the data
text_split = text_replaced.split()

# How is this different from tokenizing the data?
text_tokens = nltk.word_tokenize(text_replaced) # Honestly looks the same

# Count the number of unique words in our dataset
len_text = len(text_tokens)
print(f"Number of words in document: {len_text}")


### Remove stop words
# start by defining the stop words
stop_words = set(stopwords.words('english'))

# Only pull in words that are NOT in stop words
text_filtered = [word for word in text_tokens if not word in stop_words]

# Check the number of unique words in our dataset
len_text_nostop = len(text_filtered)
print(f"Number of non stop-words in document: {len_text_nostop}")


# There are some other weird words popping up, that we need to remove
additional_stop_words = ['shall', 'may']

text_filtered_again = [word for word in text_filtered if not word in additional_stop_words]

# Check the number of unique words in our dataset
len_text_cleanwords = len(text_filtered_again)
print(f"Number of non stop-words in document: {len_text_cleanwords}")





######################################
###            Word Count          ###
######################################
# In this section, we count the frequency
# (i.e. the number of times) each word
# appears in the text. We then visualize
# our data using matplotlib.


# Let's use nltk's FreqDist function to count the occurrences of each word
text_freq = nltk.FreqDist(text_filtered_again)

# What's the most common word?
counts = text_freq.most_common(20)
print(f"Our top {len(counts)} words, and their associated frequencies, are:\n{counts}")


# Let's try converting the frequency distribution to a pandas dataframe
text_freq_df = pd.DataFrame(counts, columns = ['words', 'count'])


### Viz time
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
text_freq_df.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="#86BC25")

# Set the title of the graph
ax.set_title("Top 20 Words Found in Use of Force Policies")

plt.show()
plt.clf()


######################################
###             Bi-Grams           ###
######################################
# In this section, we count the frequency
# of ordinal pairs of words occurring together.
# This will provide further insight into
# combinations of words that are likely
# to occur together.

# Count our unique word pairs and put it into list form
text_bigrams = list(nltk.bigrams(text_filtered_again))

# Create counter of words in clean bigrams
bigram_counts = collections.Counter(text_bigrams)

# How many word-pairs do we want to show?
num = 25

# What's the most common pair of words?
bi_counts = bigram_counts.most_common(num)
print(f"Our top {len(bi_counts)} words, and their associated frequencies, are:\n{bi_counts}")


# Let's try converting the frequency distribution to a pandas dataframe
text_bigram_df = pd.DataFrame(bi_counts, columns = ['word_pairs', 'count'])


### Viz time
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
text_bigram_df.sort_values(by='count').plot.barh(x='word_pairs',
                      y='count',
                      ax=ax,
                      # Deloitte Green
                      color="#86BC25")

# Set the title of the graph
ax.set_title(f"Top {num} Word Pairs Found in Use of Force Policies")

plt.show()
plt.clf()


