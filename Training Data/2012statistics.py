import pandas as pd
from candidateaffiliation import Candidatesimilarity


Candidate=Candidatesimilarity()



df=pd.read_csv("../Processed Election Data/voterdata2012_updated.csv")

statelist=df["State"].drop_duplicates()

states=statelist.as_matrix()

stateswin=[]
stateslost=[]
for state in states:
    statewise=df[df["State"]==states]
    result=statewise[statewise["Percent"]>0.5]
    name=result["Candidate"].as_matrix()
    name=name[0]
    if name==Candidate:
        stateswin.append(state)
    else:
        stateslost.append(state)

def statelist():
    return stateswin,stateslost



