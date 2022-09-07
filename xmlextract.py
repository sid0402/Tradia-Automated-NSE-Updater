import xml.etree.ElementTree as ET
import pandas as pd

file = '/Users/siddhantagarwal/Desktop/example1.xml'

tree = ET.parse(file)
root = tree.getroot()

'''
To understand each element:

x = 'DilutedEarningsLossPerShareFromContinuingAndDiscontinuedOperations'

print([elem.tag for elem in root.iter('{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}'+str(x))])
print([elem.attrib for elem in root.iter('{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}'+str(x))])
print([elem.text for elem in root.iter('{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}'+str(x))])
'''

#EXTRACTING COMPANY NAME
company_name = [elem.text for elem in root.iter('{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}Symbol')][0]

#EXTRACTING DATE FOR PROFIT, INCOME, EXPENSES, BASIC EPS, DILUTED EPS
keytags = ['ProfitLossForPeriod', 'Income','Expenses','BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations','DilutedEarningsLossPerShareFromContinuingAndDiscontinuedOperations']
my_dict = {}
for i in keytags:
    a = [elem.text for elem in root.iter('{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}'+str(i))][0]
    my_dict[i] = a 

#MAKING DATAFRAME FOR DATA
df = pd.DataFrame.from_dict(my_dict,orient = 'index')
df.columns = [company_name]
df.rename(index = {'ProfitLossForPeriod':'Net Profit/Loss','Income':'Total Income','Expenses':'Total Expenses','BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations':'Basic EPS','DilutedEarningsLossPerShareFromContinuingAndDiscontinuedOperations':'Diluted EPS'}, inplace = True)
print(df)

#CREATING EXCEL FILE
df.to_excel('GMBREW EXAMPLE.xlsx')

'''
tag names:
    
- ProfitLossForPeriod [0]
- Income [0]
- Expenses [0]
- BasicEarningsLossPerShareFromContinuingOperations
- DilutedEarningsLossPerShareFromContinuingOperations
- BasicEarningsLossPerShareFromContinuingAndDiscontinuedOperations [0]
- DilutedEarningsLossPerShareFromContinuingAndDiscontinuedOperations [0]
'''