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



######################################
###           Read in Data         ###
######################################
# Change the working directory
os.chdir(r'C:\Users\jschulberg\Documents\Learning\NLP\NLS Mentorship Program\NLP-Use-of-Force\Data')
os.getcwd()

# First find the names of the files we have
os.listdir()


baltimore_data = open("Baltimore.txt", "r")

# Read the lines of the file
baltimore_txt = baltimore_data.readlines()
print(baltimore_txt[0:100])

type(baltimore_txt) # Our data is in list format

######################################
###     Text Pre-processing        ###
######################################
# Make all the text lowercase
balt_lower = baltimore_txt[0].lower()

# Remove numbers
balt_chars = re.sub(r"[0-9]", "", balt_lower)

# Split the data
balt_split = balt_chars.split()

# How is this different from tokenizing the data?
balt_tokens = nltk.word_tokenize(balt_chars) # Honestly looks the same

# Count the number of unique words in our dataset
len_balt = len(balt_tokens)
print(f"Number of words in document: {len_balt}")


### Remove stop words
# start by defining the stop words
stop_words = set(stopwords.words('english'))

# Only pull in words that are NOT in stop words
balt_filtered = [word for word in balt_tokens if not word in stop_words]

len_balt_nostop = len(balt_filtered)
print(f"Number of non stop-words in document: {len_balt_nostop}")


######################################
###            Word Count          ###
######################################
# Let's loop through our dataset and count everything using counter
balt_count = Counter(word.lower() for word in balt_filtered)


balt_freq = nltk.FreqDist(balt_filtered)

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
                      color="green")

ax.set_title("Top 20 Words Found in Baltimore Use of Force Policy")

plt.show()
plt.clf()
