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
os.chdir(r'C:\Users\jschulberg\Documents\Learning\NLP\NLS Mentorship Program\NLP-Use-of-Force\Data\Processed_Text')
os.getcwd()

# First find the names of the files we have
os.listdir()


baltimore_data = open("Memphis.txt", "r")

# Read the lines of the file
baltimore_txt = baltimore_data.readlines()
print(baltimore_txt[0:100])

type(baltimore_txt) # Our data is in list format

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
balt_lower = baltimore_txt[0].lower()

# Remove numbers
balt_chars = re.sub(r"[0-9]", "", balt_lower)

# Remove punctuation
balt_chars = re.sub(r'[^\w\s]', '', balt_chars)

### Fix words that were read in improperly
# There are a few words that are being read in improperly due to
# the conversion from PDF to TXT files. This can either look like
# an unneeded space separating a single word (i.e. de escalation)
# or the concatenation of two words that should be separated (i.e
# forcelethal). Because of this, we'll manually replace the words
# that appear most frequently in these forms.

# 'e scalation' --> 'escalation'
balt_replaced = re.sub(r'e.scalation', 'escalation', balt_chars)
# 'de escalation' --> 'deescalation'
balt_replaced = re.sub(r'de.escalation', 'deescalation', balt_chars)
# 'f orce' --> 'force'
# balt_replaced = re.sub(r'\s[f]\s[orce]', 'force', balt_replaced)
balt_replaced = re.sub(r'f.orce', 'force', balt_replaced)
# 'forcelethal' --> 'force lethal'
balt_replaced = re.sub(r'\sforcelethal', 'force lethal', balt_replaced)
# 'n eccessary' --> 'neccessary'
balt_replaced = re.sub(r'n.ecessary', 'necessary', balt_replaced)
# 'deadlyforce' --> 'deadly force'
balt_replaced = re.sub(r'\sdeadlyforce', 'deadly force', balt_replaced)
# 'excessiv e' --> 'excessive'
balt_replaced = re.sub(r'excessiv.e', 'excessiv.e', balt_replaced)
# 'm embers' --> 'members'
balt_replaced = re.sub(r'm.embers', 'members', balt_replaced)
# 'r eview' --> 'review'
balt_replaced = re.sub(r'r.eview', 'review', balt_replaced)
# 'p roportional' --> 'proportional'
balt_replaced = re.sub(r'p.roportional', 'proportional', balt_replaced)
# 'resi stance' --> 'resistance'
balt_replaced = re.sub(r'resi.stance', 'resistance', balt_replaced)
# 'r easonable' --> 'reasonable'
balt_replaced = re.sub(r'resi.stance', 'resistance', balt_replaced)
# 'd eadly' --> 'deadly'
balt_replaced = re.sub(r'd.eadly', 'deadly', balt_replaced)
# 'u se' --> 'use'
balt_replaced = re.sub(r'u.se', 'use', balt_replaced)
# 'g eneral' --> 'general'
balt_replaced = re.sub(r'g.eneral', 'general', balt_replaced)
# 'v olume' --> 'volume'
balt_replaced = re.sub(r'v.olume', 'volume', balt_replaced)
# 'f ebruary' --> 'february'
balt_replaced = re.sub(r'f.ebruary', 'february', balt_replaced)
# 'februar y' --> 'february'
balt_replaced = re.sub(r'februar.y', 'february', balt_replaced)
# 'p rocedures' --> 'procedures'
balt_replaced = re.sub(r'p.rocedures', 'procedures', balt_replaced)
# 'o perating' --> 'operating'
balt_replaced = re.sub(r'o.perating', 'operating', balt_replaced)
# 'o rder' --> 'order'
balt_replaced = re.sub(r'o.rder', 'order', balt_replaced)
# 'p olice' --> 'police'
balt_replaced = re.sub(r'p.olice', 'police', balt_replaced)
# 'd epartment' --> 'department'
balt_replaced = re.sub(r'o.rder', 'order', balt_replaced)
# 'b oard' --> 'board'
balt_replaced = re.sub(r'b.oard', 'board', balt_replaced)
# 't ucson' --> 'tucson'
balt_replaced = re.sub(r't.ucson', 'tucson', balt_replaced)





### Tokenize text
# Split the data
balt_split = balt_replaced.split()

# How is this different from tokenizing the data?
balt_tokens = nltk.word_tokenize(balt_replaced) # Honestly looks the same

# Count the number of unique words in our dataset
len_balt = len(balt_tokens)
print(f"Number of words in document: {len_balt}")


### Remove stop words
# start by defining the stop words
stop_words = set(stopwords.words('english'))

# Only pull in words that are NOT in stop words
balt_filtered = [word for word in balt_tokens if not word in stop_words]

# Check the number of unique words in our dataset
len_balt_nostop = len(balt_filtered)
print(f"Number of non stop-words in document: {len_balt_nostop}")


# There are some other weird words popping up, that we need to remove
additional_stop_words = ['shall', 'may']

balt_filtered_again = [word for word in balt_filtered if not word in additional_stop_words]

# Check the number of unique words in our dataset
len_balt_cleanwords = len(balt_filtered_again)
print(f"Number of non stop-words in document: {len_balt_cleanwords}")





######################################
###            Word Count          ###
######################################
# In this section, we count the frequency
# (i.e. the number of times) each word
# appears in the text. We then visualize
# our data using matplotlib.


# Let's use nltk's FreqDist function to count the occurrences of each word
balt_freq = nltk.FreqDist(balt_filtered_again)

# What's the most common word?
counts = balt_freq.most_common(20)
print(f"Our top {len(counts)} words, and their associated frequencies, are:\n{counts}")


# Let's try converting the frequency distribution to a pandas dataframe
balt_freq_df = pd.DataFrame(counts, columns = ['words', 'count'])


### Viz time
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
balt_freq_df.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="#86BC25")

# Set the title of the graph
ax.set_title("Top 20 Words Found in Baltimore Use of Force Policy")

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
balt_bigrams = list(nltk.bigrams(balt_filtered_again))

# Create counter of words in clean bigrams
bigram_counts = collections.Counter(balt_bigrams)

# How many word-pairs do we want to show?
num = 25

# What's the most common pair of words?
bi_counts = bigram_counts.most_common(num)
print(f"Our top {len(bi_counts)} words, and their associated frequencies, are:\n{bi_counts}")


# Let's try converting the frequency distribution to a pandas dataframe
balt_bigram_df = pd.DataFrame(bi_counts, columns = ['word_pairs', 'count'])


### Viz time
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
balt_bigram_df.sort_values(by='count').plot.barh(x='word_pairs',
                      y='count',
                      ax=ax,
                      # Deloitte Green
                      color="#86BC25")

# Set the title of the graph
ax.set_title(f"Top {num} Word Pairs Found in Baltimore Use of Force Policy")

plt.show()
plt.clf()


