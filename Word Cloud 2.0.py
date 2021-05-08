# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:44 2020

@author: Nadun
"""


import PyPDF2 
import textract
import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os

#Import keywords
keywords = pd.read_excel('location for the keywords file xlsx')
keywords = keywords.apply(lambda x: x.astype(str).str.lower())
terms = keywords["Terms"].tolist()


file_in = 'location for the pdf file'
file_split = file_in.split(".")
pdfFileObj = open(file_in,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
enc=pdfReader.isEncrypted

if enc is True:
    print ("File is encrypted")
else:
    print ("File is not encryptd. Wait till the program process it.")
    num_pages = pdfReader.numPages
    count = 0
    text = ""
     
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    if text != "":
        text = text
    else:
        text = textract.process(file_in, method='tesseract', language='eng')
        
    
    text = text.replace('\n', '') 
    text = text.lower()
    
    temp = []
    def sent_append(wordLi):
        for i in wordLi:
            if i in text:
                scr_sent = re.findall(i,text)
                temp.append(scr_sent)
            
    sent_append(terms)
    
    temp = [j for i in temp for j in i]
    temp.sort()
    
    df = pd.DataFrame(temp,columns =['Terms']) 
    termfqw = (df['Terms'][:]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
    termfqw.columns = ['Word','Frequency']
    termfqw = termfqw.sort_values('Frequency', ascending = False)
    termfqw.to_csv(os.path.join(file_split[0] +".csv"))

    stopwords = set(STOPWORDS)
    stopwords.update(["Columns", "DataFrame", "Index", "Empty","Frequency","Word"])
    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        colormap="Blues",
        background_color = 'white',
        stopwords = stopwords).generate(str(termfqw))
    fig = plt.figure(
        figsize = (10, 7),
        facecolor = 'white',
        edgecolor = 'black')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    #plt.show()
    path_out = os.path.join(file_split[0] + ".png")
    wordcloud.to_file(path_out)
        

print ("Process Completed!")



