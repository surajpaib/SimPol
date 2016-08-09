import pandas as pd
from candidateaffiliation import Candidatesimilarity


Candidate=Candidatesimilarity()



df=pd.read_csv("../Processed Election Data/voterdata2012_updated.csv")

statelist=df["State"].drop_duplicates()

states=statelist.as_matrix()

stateswin=[]
stateslost=[]
for state in states:
    statewise=df[df["State"]==state]
    result=statewise[statewise["Percent"]>0.5]
    name=result["Candidate"].as_matrix()
    name=name[0]
    if name==Candidate:
        stateswin.append(state)
    else:
        stateslost.append(state)



if Candidate=='Barack':
    print " You can win the next US Elections \n"

    print "States Won:\n"
    print stateswin
    print "States Lost:\n"
    print stateslost

else:
    print " You probably won't win the next US Elections \n"

    print "States Won:\n"
    print stateswin
    print "States Lost:\n"
    print stateslost




