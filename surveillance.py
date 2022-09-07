import PyPDF2
import tabula
import pandas as pd

file = '/Users/siddhantagarwal/Desktop/CV/Tradia/surv2.pdf'
pdfFileObj = open(file,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pg_text = []
for i in range(pdfReader.getNumPages()):
    text = [pdfReader.getPage(i).extractText()]
    text = text[0].split('\n')
    pg_i = []
    for i in text:
        if i.strip():
            pg_i.append(i)
    pg_text.append(pg_i)
    
print(len(pg_text))

#### DATE ###################
months = ['january','february','march','april','may','june','july','august', 'september','october','november','december']
months = [i.capitalize() for i in months]

pg = pg_text[0]

dates = []
for i in pg:
    for j in months:
        if j in i:
            date = i
            #print(date)
            dates.append(date)
            
date = dates[0]      
print("DATE: ",date)
#### COMPANY #####################
all_companies = []
for pg in pg_text:
    companies = []
    for i in range(len(pg)):
        if "No." in pg[i]:
            companies.append(pg[i+1])
    companies = [i.strip('Clarification by') for i in companies]
    all_companies.append(companies)
#print(all_companies)
companies = []
for i in all_companies:
    for j in i:
        companies.append(j)
#print(companies)

################ CONTENT ######################
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

#print(content)

############# CREATING DICTIONARY #########
company_dict = {}

for i in range(len(companies)):
    company_dict[companies[i]] = content[i]
#print(company_dict)

for i in company_dict:
    for j in company_dict[i]:
        if ("Significant" or "Significant increase/decrease in" or "Significant increase in" or "Significant decrease" or "increase/decrease" or "increase" or "decrease") in j:
            company_dict[i] = j
            break

print(company_dict) 


