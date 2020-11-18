# NLP-Use-of-Force
This repository focuses on Natural Language Processing (NLP) analysis on Police Use of Force Policies. The dataset to these policies can be found [here](http://useofforceproject.org/database).
In this analysis, we use PDF text extraction techniques to build the text datasets that are later used for NLP analysis. In terms of NLP, this project utilizes the following methods:
 - Word Frequency
 - Bi-gram Analysis
 - Topic Modeling
 - Cosine Similarity

## Purpose
We aim to answer some of the following questions:
 - How does language in Police Use of Force policies differ between major US cities? 
 - Does language in these policies affect outcomes in trends related to police-caused fatalities?

The results of this project/case study will:
 - Compare and determine the similarity of language used in Police Use of Force policies across major US cities
 - Analyze most frequent words and topics within Use of Force policies
 - Identify specific language that led to positive and negative use of force outcomes
 - Provide suggestions for changing language in Police Use of Force policies

## Our Approach
**Data Collection & Pre-processing**
 - Collect Use of Force policies from 100 largest police departments in U.S.
 - Scrape text from policies, including PDF scraping techniques for policies in PDF format
 - Normalize, tokenize, and lemmatize text
 - Removal of stop words and insignificant words

**Basic NLP Analysis**  
Key text summary statistics, including:
 - Number of documents analyzed
 - Total words across all documents
 - Average words per document
 - Word frequencies
 - Bi-gram analysis

**Advanced NLP Similarity Analysis**
 - Topic modeling to identify recurrent themes amongst successful policies
 - Cosine similarity to quantify language similarity between policies in 100 cities to an "ideal policy" 

