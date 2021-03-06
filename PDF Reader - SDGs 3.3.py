# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:26:34 2020

@author: Nadun
"""

#Import libraries
import PyPDF2 
import textract
import re
import pandas as pd
import os

#Import keywords
path = os.getcwd()+ '\keywords.xlsx'
keywords = pd.read_excel(path)
keywords = keywords.apply(lambda x: x.astype(str).str.lower())
l1 = keywords["SDG 1"]
l2 = keywords["SDG 2"]
l3 = keywords["SDG 3"]
l4 = keywords["SDG 4"]
l5 = keywords["SDG 5"]
l6 = keywords["SDG 6"]
l7 = keywords["SDG 7"]
l8 = keywords["SDG 8"]
l9 = keywords["SDG 9"]
l10 = keywords["SDG 10"]
l11 = keywords["SDG 11"]
l12 = keywords["SDG 12"]
l13 = keywords["SDG 13"]
l14 = keywords["SDG 14"]
l15 = keywords["SDG 15"]
l16 = keywords["SDG 16"]
l17 = keywords["SDG 17"]

#Import sustainability report
#For the demonstration purposes, I have used the Sustainability report of Dialog - 2019
filename = os.getcwd()+ '\Dialog sustainability-report-2019.pdf' 
#Read pdf
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
enc=pdfReader.isEncrypted

if enc is False:
    print ("Report is not encryptd. Wait till the program process it.")
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
       text = textract.process(filename, method='tesseract', language='eng')
       text = text.replace('\n', '')  
    
    sent = []
    sdg = []
    
    def sent_append(wordLi,sd):
        for i in wordLi:
            if i in text:
                #scr_sent = re.findall(r"([A-Z][^\.!?]*[\.!?])"+i+"(?=[\s.,?!])[^.?!]*[.?!])",text)

                #pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
                #scr_sent=pat.findall(text)
                scr_sent = re.findall(r"([^.?!]*(?<=[.,?\s!])"+i+"(?=[\s.,?!])[^.?!]*[.?!])",text)

                sent.append(scr_sent)
                sdgn = ('SDG '+str(sd))
                sdg.append(sdgn)
else:
    print ("Report is encrypted. Try again after decrypting.")
#Write the sentences           
sent_append(l1,1)  
sent_append(l2,2)  
sent_append(l3,3)                
sent_append(l4,4)
sent_append(l5,5)
sent_append(l6,6)
sent_append(l7,7)
sent_append(l8,8)
sent_append(l9,9)
sent_append(l10,10)
sent_append(l11,11)
sent_append(l12,12)
sent_append(l13,13)
sent_append(l14,14)
sent_append(l15,15)
sent_append(l16,16)
sent_append(l17,17)
                    
con_l1 = [j for i in sent for j in i]
finaldf = pd.DataFrame(list(zip(con_l1, sdg)),columns=['Sentence','SDG'])

#Removing the commonly found nuisance characters
finaldf= finaldf.replace({'\n':''}, regex=True)
finaldf= finaldf.replace({'\??':''}, regex=True)
finaldf= finaldf.replace({'?????Kerry':''}, regex=True)
finaldf= finaldf.replace({'?????Fred':''}, regex=True)
finaldf.drop_duplicates(keep='first', inplace=True)

#Writing to excel
path = os.getcwd()+ '\Dialog SDGs.xlsx'
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
finaldf.to_excel(writer, sheet_name = 'List',index = None)
writer.save()
writer.close()  


