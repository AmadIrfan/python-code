from UI import UI
from Muser import Muser


class AdminUI:
    def adminMenu():
        # manu_top1()
        print(" Main Manu > Admin ")
        # lines()
        print("(1) : ADD Admin")
        print("(2) : Add Cars")
        print("(3) : Delete Cars")
        print("(4) : Show Users & Admin")
        print("(5) : Show All Cars")
        print("(6) : Generate Reports")
        print("(7) : Log Out")
        adminInput = input("Input : ")
        return int(adminInput)

    def addAdmin():
        print(" Main Manu > Admin >Add admin ")
        UI.lines()
        adid = int(input("Enter Admin ID "))
        adfname = input("Enter Admin first Name ")
        aduname = input("Enter Admin user Name ")
        adpass = input("Enter Admin Password ")
        ad_city = input("Enter admin city ")
        ad_gender = input("Enter Admin gender ")
        user = Muser(adid, aduname, adfname, adpass, ad_gender, ad_city, "Admin")
        return user
