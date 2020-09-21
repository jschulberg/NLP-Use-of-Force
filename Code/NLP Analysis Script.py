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
from collections import Counter # Helps with word counts



######################################
###           Read in Data         ###
######################################
# Change the working directory
os.chdir(r'C:\Users\jschulberg\Documents\Learning\NLP\NLS Mentorship Program\NLP-Use-of-Force\Data')
os.getcwd()

# First find the names of the files we have
os.listdir()

# Open each and save it into a dataframe
# files = []
# for file in os.listdir():
#     files.append(file)
#     file_name = file
#     print(file)

# print(files)

baltimore_data = open("Baltimore.txt", "r")

# Read the lines of the file
baltimore_txt = baltimore_data.readlines()
print(baltimore_txt)

type(baltimore_txt) # Our data is in list format

######################################
###            Word Count          ###
######################################
# Split the data
baltimore_split = baltimore_txt[0].split()

######################################
###            Word Count          ###
######################################
# Let's loop through our dataset and count everything using counter
Counter(word.lower() for word in baltimore_split)
