import PyPDF2
import tabula
import pandas as pd

file = '/Users/siddhantagarwal/Desktop/CV/Tradia/clearance1.pdf'
pdfFileObj = open(file,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)

pg_text = []
for i in range(pdfReader.getNumPages()):
    text = [pdfReader.getPage(i).extractText()]
    text = text[0].split('\n')
    pg_i = []
    for i in text:
        if i.strip():
            pg_i.append(i)
    pg_text.append(pg_i)
    
#print(pg_text)

'''
text = [pdfReader.getPage(0).extractText()]
text = text[0].split('\n')
pg = []
for i in text:
    if i.strip():
        pg.append(i)


print(pg_text)
'''
########### DATE ####################
'''
pg = pg_text[0]
months = ['january','february','march','april','may','june','july','august', 'september','october','november','december']
months = [i.capitalize() for i in months]
brackets = ['(',')']
date = []
i = 0
while (i <= len(pg)):
    if pg[i] in brackets:
        date.append(pg[i])
        flag = True
        while flag==True:
            i = i+1
            if not(pg[i] in brackets):
                date.append(pg[i])
            else:
                date.append(pg[i])
                flag = False

print("DATE: ",date)
##################################################
'''
############# CONTENT ####################
content = []

for pg in pg_text:
    for i in range(len(pg)):
        content_i = []
        if 'Press Release No.' in pg[i]:
            j = i+1
            while not('Press Release No.' in pg[j]):
                content_i.append(pg[j])
                j += 1
                if j == len(pg):
                    break
            content.append(content_i)

print(content)
# ONCE YOU GET COMPANY LIST, CHECK FOR THE NAME OF THE COMPANY 
# IN THE LIST PG
# TITLE IS THE JUST "MARKET WIDE POSITION LIMIT IN <COMPANY NAME>

################# STATS ##########################
stat_elements = [str(i) for i in range(10)]
stat_elements.append('%')
stat_elements.append('$')
print(stat_elements)

all_stats = []
for content_i in content:
    content_stats = []
    for i in content_i:
        for j in stat_elements:
            if j in i:
                content_stats.append(i)
                break
    all_stats.append(content_stats)
print(all_stats)

###### CREATING DICTIONARY #############

