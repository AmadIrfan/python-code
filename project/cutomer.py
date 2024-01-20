
class Customer:
    customerfname= ""
    customerlname=""
    customeruname=""
    customerpass=""
    customergender=""
    customercity=""
    customeradress=""
    
    def __init__(self,name,lname,cname,cpass,cgen,ccity,cadress):
        self.customerfname=name
        self.customerlname=lname
        self.customeruname=cname
        self.customerpass=cpass
        self.customergender=cgen
        self.customercity=ccity
        self.customeradress=cadress
