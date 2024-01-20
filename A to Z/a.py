from One import Ones
import pandas as pd
import random as r
# c = Ones("amad", 15)
# c.printer()
arr=[]
for i in range(0,10):   
    nam=r.randint(10,60)
    arr.append(nam)

pf=pd.DataFrame({'List ':arr},index=None)
pf.to_csv('a.csv')