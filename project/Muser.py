class Muser:
    Uid = ""
    fName = ""
    LoginName = ""
    LoginPassWord = ""
    Role = ""
    UGender = ""
    UCity = ""
    def __init__(self,Uid, name,fname, password, Gender, City, role):
        self.Uid=Uid
        self.fName=fname
        self.LoginName = name
        self.LoginPassWord = password
        self.Role = role
        self.UCity = City
        self.UGender = Gender
