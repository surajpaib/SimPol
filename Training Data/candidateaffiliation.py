from artificialdatasets import meanvalues
import math


obama,gary,jill,mitt,issues=meanvalues()



print "Enter your stand on the following issues, (-2 indicates Strongly disagree, -1 : Disagree, 0 : Neutral, 1: Agree , 2 : Strongly Agree)\n\n"




ipvec=[]

for i in range(len(obama)):
    q=raw_input(issues[i]+"\n")
    q=int(q)
    if (q==-1)or(q==-2)or(q==0)or(q==1)or(q==2):

        ipvec.append(q)
    else:
        while (q!=-1)and(q!=-2)and(q!=0)and(q!=1)and(q!=2):
            print "Please Re-enter a Valid Choice"
            q = raw_input(issues[i]+"\n")
            q = int(q)
        ipvec.append(q)

obamametric=0
garymetric=0
jillmetric=0
mittmetric=0
for i in range(len(issues)):
    obamametric=float(obamametric+math.pow((obama[i]-ipvec[i]),4))
    garymetric = float(garymetric + math.pow((gary[i]-ipvec[i]),4))
    jillmetric = float(jillmetric + math.pow((jill[i]-ipvec[i]),4))
    mittmetric = float(mittmetric + math.pow((mitt[i]-ipvec[i]),4))


k=min(obamametric,garymetric,jillmetric,mittmetric)

if k==obamametric:
    Candidate='Barack'

if k==garymetric:
    Candidate='Gary'

if k==jillmetric:
    Candidate='Jill'

if k==mittmetric:
    Candidate='Mitt'



def Candidatesimilarity():
    return Candidate



