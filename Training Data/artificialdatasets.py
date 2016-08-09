


import pandas as pd






df1=pd.read_csv("Barack_num.csv",header=None,names=["Issues","Stand"])
df2=pd.read_csv("Gary_num.csv",header=None,names=["Issues","Stand"])
df3=pd.read_csv("Jill_num.csv",header=None,names=["Issues","Stand"])
df4=pd.read_csv("Mitt_num.csv",header=None,names=["Issues","Stand"])


issues=df1.Issues
issues=issues.as_matrix()
stand=df1.Stand
stand=stand.as_matrix()
stand2=df2.Stand
stand2=stand2.as_matrix()
stand3=df3.Stand
stand3=stand3.as_matrix()
stand4=df4.Stand
stand4=stand4.as_matrix()




def meanvalues():

    return stand,stand2,stand3,stand4,issues