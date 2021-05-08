# PDF-scraping
The project consist of mainly 2 phases; data extraction from pdf's and text visualization in a form of a word cloud.

Sustainable Development Goals (SDGs) have been introduced by the UN. At present, companies as well as investors pay attention to sustainable investments. 
This program is coded in order to capture the context that the comapnies are discussing in their sustainability/ annual reports addressing the SDGs. In order to fetch the sentences, I have used a pre-compiled keyword list which has is provided by United Nations Sustainable Development Solutions Network http://ap-unsdsn.org/wp-content/uploads/2017/04/Compiled-Keywords-for-SDG-Mapping_Final_17-05-10.xlsx

# Codes
# 1 - PDF Scraping
The python code "PDF Reader - SDGs 3.3.py" will capture all the sentences which include the keywords mentioned in the given keyword list and very minor level of data cleaning is included. A sample output file has been provided "Test.xlsx".

# 2 - Visualization
The python code "Word Cloud 2.0" is to get the number of times a term mentioned in the keyword file appears on the pdf, and based on the number of occurrences a word cloud will be created. A sample image is provided "wordcloud.png".
