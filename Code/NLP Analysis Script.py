# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:57:08 2020

@author: jschulberg
"""

# Import packages
import os # Helps work with directories

### Read in data
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
print(f.read())
