import csv

file1=open("Barack Obama.csv",'r+b')
file2=open("Mitt Romney.csv",'r+b')
file3=open("Jill Stein.csv",'r+b')
file4=open("Gary Johnson.csv",'r+b')
path_1="C:\Users\Suraj\OneDrive\Documents\SimPol\SimPol\Training Data\Barack_num.csv"
path_2="C:\Users\Suraj\OneDrive\Documents\SimPol\SimPol\Training Data\Mitt_num.csv"
path_3="C:\Users\Suraj\OneDrive\Documents\SimPol\SimPol\Training Data\Jill_num.csv"
path_4="C:\Users\Suraj\OneDrive\Documents\SimPol\SimPol\Training Data\Gary_num.csv"
wfile1=open(path_1,'wb')
wfile2=open(path_2,'wb')
wfile3=open(path_3,'wb')
wfile4=open(path_4,'wb')
reader1=csv.reader(file1)
reader2=csv.reader(file2)
reader3=csv.reader(file3)
reader4=csv.reader(file4)
writer1=csv.writer(wfile1)
writer2=csv.writer(wfile2)
writer3=csv.writer(wfile3)
writer4=csv.writer(wfile4)

for row in reader1:
    if(row[1]=="Strongly Favors"):
        row[1]=2
    if(row[1]=="Favors"):
        row[1]=1
    if(row[1]=="No opinion on"):
        row[1]=0
    if(row[1]=="Neutral on"):
        row[1]=0
    if(row[1]=="Opposes"):
        row[1]=-1
    if(row[1]=="Strongly Opposes"):
        row[1]=-2


    writer1.writerow(row)


for row in reader2:
        if(row[1]=="Strongly Favors"):
            row[1]=2
        if(row[1]=="Favors"):
            row[1]=1
        if(row[1]=="No opinion on"):
            row[1]=0
        if(row[1]=="Neutral on"):
            row[1]=0
        if(row[1]=="Opposes"):
            row[1]=-1
        if(row[1]=="Strongly Opposes"):
            row[1]=-2


        writer2.writerow(row)

        
for row in reader3:
    if(row[1]=="Strongly Favors"):
        row[1]=2
    if(row[1]=="Favors"):
        row[1]=1
    if(row[1]=="No opinion on"):
        row[1]=0
    if(row[1]=="Neutral on"):
        row[1]=0
    if(row[1]=="Opposes"):
        row[1]=-1
    if(row[1]=="Strongly Opposes"):
        row[1]=-2


    writer3.writerow(row)

for row in reader4:
    if(row[1]=="Strongly Favors"):
        row[1]=2
    if(row[1]=="Favors"):
        row[1]=1
    if(row[1]=="No opinion on"):
        row[1]=0
    if(row[1]=="Neutral on"):
        row[1]=0
    if(row[1]=="Opposes"):
        row[1]=-1
    if(row[1]=="Strongly Opposes"):
        row[1]=-2


    writer4.writerow(row)


wfile1.close()
wfile2.close()
wfile3.close()
wfile4.close()
