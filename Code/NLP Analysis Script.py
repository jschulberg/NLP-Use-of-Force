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

# Count everything in a dictionary format
# def simple_count(tokens):
#     count_dict = {}
#     for token in tokens:
#         count_dict[token] += 1
#     return count_dict

# simple_count(balt_tokens)

# def count_frequencies(word_list):
#     # Calculate word frequencies
#     word_freq = [word_list.count(word) for word in word_list]
#     # Zip together words + word frequencies into the same dict
#     return dict(list(zip(word_list, word_freq)))

balt_freq = nltk.FreqDist(balt_filtered)

# What's the most common word?
counts = balt_freq.most_common(25)
print(f"Our top {len(counts)} words, and their associated frequencies, are:\n{counts}")


labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.35

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()
