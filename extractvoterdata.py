import xlrd
import csv
workbook=xlrd.open_workbook('2004pres.xls', on_demand=True)
worksheet=workbook.sheet_by_name('2004 PRES GENERAL RESULTS')

row=482
candidate_data=[]




for index in range(row):
    temp=[]
    temp.append(worksheet.cell(index,2).value)
    temp.append(worksheet.cell(index,5).value)
    temp.append(worksheet.cell(index,12).value)
    candidate_data.append(temp)

print(candidate_data[0:5])

ifile=open("voterdata2004.csv",'wb')
writer=csv.writer(ifile,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)

for row in candidate_data:
    if row[1]=='':
        candidate_data.remove(row)


for row in candidate_data:
    writer.writerow(row)

ifile.close()
