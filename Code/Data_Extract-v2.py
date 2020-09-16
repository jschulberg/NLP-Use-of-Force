
# coding: utf-8

# ### Libraries

# In[28]:


import os
import nltk
import io
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import TextConverter
import PyPDF2

# pip install pdfminer.six


# ### Identify and get PDF files to extract text from

# In[3]:


# Check our working directory
os.getcwd()


# In[4]:


# Set our working directory to where our files are located
os.chdir('C:\\Users\\ftinelli\\Documents\\Python Scripts\\NLS_Mentorship_Program\\Data')


# In[25]:


# Get all the PDF files in cwd.
pdf_files = []

for filename in os.listdir('.'): # Go through all files that end with .pdf in cwd and add to list.
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_files


# ### Open each PDF and convert context to string from each PDF

# In[29]:


# Loop through each of the PDF files.
for filename in pdf_files:
    
    # PDFminer variables and components.
    resource_manager = PDFResourceManager()
    output_string = io.StringIO()
    converter = TextConverter(resource_manager, output_string, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    pdfFileObj = open(filename, 'rb') # allows you to read the file.

    
    # Loop through each page of each PDF file.
    for page in PDFPage.get_pages(pdfFileObj,caching=True,check_extractable=True):
        page_interpreter.process_page(page)
    text = output_string.getvalue()
    
    # close open handles
    converter.close()
    output_string.close()

    # Save extracted text to a text file.
    text_file = open(filename + '_Extract.txt','w', encoding="utf-8") # open to output file and overwrite if it exists.
    text_file.write(text)
    text_file.close()
    
    print(filename)
    print(text_file)
    print('\n')

