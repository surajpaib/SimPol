import csv

ifile=open('voterdata2004.csv','rb')
reader=csv.reader(ifile)
name_list=["George W.","John F.","Ralph","Michael","David","Leonard"]
candidate_data=[]

for row in reader:
    for name in name_list:
        if (row[1]==name):
            candidate_data.append(row)


ofile=open('voterdata2004_updated.csv','wb')
writer=csv.writer(ofile,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)


for row in candidate_data:
    writer.writerow(row)

ifile.close()
