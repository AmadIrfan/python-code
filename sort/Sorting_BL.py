class Medicine:
    Medicine_Name=''
    Medicine_MF=''
    Medicine_MW=''
    IUPAC_Name=''
    Compound_CID=''
    Create_Date=''
    
    def __init__(self, name,mf,mw,Iupac_name,Compound_cid,create_Date):
        self.Medicine_Name=name
        self.Medicine_MF=mf
        self.Medicine_MW=mw
        self.IUPAC_Name=Iupac_name
        self.Compound_CID=Compound_cid
        self.Create_Date=create_Date
        
    def init(self, name):
        self.Medicine_Name = name

    def init(self, mf):
        self.Medicine_MF = mf

    def init(self, mw):
        self.Medicine_MW = mw

    def init(self,Iupac_name ):
        self.IUPAC_Name = Iupac_name

    def init(self, Compound_cid):
        self.Compound_CID = Compound_cid

    def init(self, create_Date):
        self.Create_Date = create_Date