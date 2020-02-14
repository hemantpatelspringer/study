import pandas as pd
import xl2dict
from xl2dict.xlextractor import XlToDict
import xlrd
from xlrd import open_workbook

# book = open_workbook("")
# sheet = book.sheet_by_index(0) #If your data is on sheet 1

from pandas import ExcelWriter
from pandas import ExcelFile

file = 'dts_daily_error_details_csg_20191224.xlsx' 
df = pd.read_excel("D:\\email\\IN\\"+file)

DOI =list( df['DOI(s)'])
Error_Type= df['Error Type']
Error_Name = df['Error Name']

print(file)
file_name,extension=file.split('.')
print(file_name)
print("Column headings:")
print(df.columns)

print(DOI)
myList = [i.split('/s')[1] for i in DOI] 
Journal_ID = [i.split('-')[0] for i in myList] 
print(Journal_ID)

teststring='Test interface: PMC DTS: '
dfSummary = pd.DataFrame({'Test': teststring,'Error Type': Error_Type, 'Error Name': Error_Name})
df['dfSummary'] = dfSummary.apply(lambda x: '{}:({}/{})'.format(x[0],x[1],x[2]), axis=1)


dfcsv = pd.DataFrame(data={"field": '',
                            "Issue Type": "QIRA Journals Request",
                            "Reporter":"qira.test",
                            "Summary":df['dfSummary'] ,
                            "Priority":'',
                            "Due Date":'',
                            "Publication Status":'20001',
                            "Production System":'20005',
                            "Error Location":'20002',
                            "Error Type":'20002',
                            "Caused by":'20025',
                            "Request Action":'20002',
                            "Error Type":'20008',
                            "Doi": DOI,
                            "ISBN/OrderNumber": '',
                            "BookID": '',
                            "Series ID/ISSN": '',
                            "Journal ID": Journal_ID,
                            "JournalVolume": '',
                            "Issue": '',
                            "Description":'',
                            "Error Name":'',                            
                            "Error Type": Error_Type,
                             "Error Name": Error_Name})
dfcsv.to_csv("D:\\email\\OUT\\"+file_name+".csv", sep=',',index=False, encoding='latin-1')


# data = pd.read_csv("D:\\email\\OUT\\"+file_name+".csv")
# print(data.head())





# my_dict = { 'name' : ["a", "b", "c", "d", "e","f", "g"],
#             'age' : [20,27, 35, 55, 18, 21, 35],
#             'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]}
# df = pd.DataFrame(my_dict)
# df.to_csv('D:\email\csv_example.csv')