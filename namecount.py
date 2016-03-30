import csv

ifile=open('voterdata2012.csv','rb')
reader=csv.reader(ifile)
name_list=["Barack","Mitt","Jill","Gary",]
candidate_data=[]

for row in reader:
    for name in name_list:
        if (row[1]==name):
            candidate_data.append(row)
        

ofile=open('voterdata2012_updated.csv','wb')
writer=csv.writer(ofile,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)


for row in candidate_data:
    writer.writerow(row)

ifile.close()
