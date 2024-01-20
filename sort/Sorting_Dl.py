import csv
import Sorting_BL
import pandas as pd

Mega_List=[]

@staticmethod
def Load_Data():
    df = pd.read_csv('Data.csv')
    Medicine_MF       =df["Medicine MF"].values.tolist()       
    Medicine_MW       =df["Medicine MW"].values.tolist()    
    Medicine_Name     =df["Medicine Name "].values.tolist()  
    IUPAC_Name        =df["IUPAC Name"].values.tolist()
    Compound_CID      =df["Compound CID "].values.tolist()
    Create_Date       =df["Create Date"].values.tolist()
    for i in range(len(Medicine_Name)):
        obj = Sorting_BL.Medicine(Medicine_Name[i], Medicine_MF[i], Medicine_MW[i], IUPAC_Name[i],
                            Compound_CID[i], Create_Date[i])
        Mega_List.append(obj)
        
def Load_Data_As_2D_Array():
    df = pd.read_csv('Data.csv')
    Medicine_MF       =df["Medicine MF"].values.tolist()       
    Medicine_MW       =df["Medicine MW"].values.tolist()    
    Medicine_Name     =df["Medicine Name "].values.tolist()  
    IUPAC_Name        =df["IUPAC Name"].values.tolist()
    Compound_CID      =df["Compound CID "].values.tolist()
    Create_Date       =df["Create Date"].values.tolist()
    return[Medicine_MF,Medicine_MW,Medicine_Name,IUPAC_Name,Compound_CID,Create_Date]