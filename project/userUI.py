from MuserDL import MuserDL
from carsDL import carsDL
from cutomer import Customer
from UI import UI
import random


class UserUI:
    def userMenu():
        #   manu_top1()
        print(" Main Manu > user")
        UI.lines()
        print("(1) : Existing")
        print("(2) : Create New Account")
        print("(3) : Main Manu")
        userInput = input("Input : ")
        return str(userInput)

    def existing_user_manu():
        #    manu_top1();
        print("Main Manu > User * ")
        #    lines();
        print(" Dashbord :--- ")
        print("(1). Show all availbile cars ")
        print("(2). Book a car ")
        print("(3). Privious record ")
        print("(4). Log out ")
        internalUser = input("Input : ")
        return str(internalUser)

    def newcustomer():
        id = random.randint(3, 9)
        customerfname = input(
            "                                 Enter your first name: ( e.g is Ahmad )"
        )
        customeruname = input(
            "                                  Enter User name:(e.g is Amad123) "
        )
        customerpass = input(
            "                                   Enter password (password consist on atleast 4)"
        )
        customergender = input(
            "                                 Enter your  Gender: (male/female)"
        )
        customercity = input("                                   Enter your  city: ")
        cust = Customer(
            id, customeruname, customerfname, customerpass, customergender, customercity
        )
        return cust

    def showAdmin():
        for obj in MuserDL.muserList:
            if obj.Role == "Admin":
                print(
                    obj.Uid
                    + "\t"
                    + obj.fName
                    + "\t"
                    + obj.LoginName
                    + "\t"
                    + obj.LoginPassWord
                    + "\t"
                    + obj.Role
                    + "\t"
                    + obj.UGender
                    + "\t"
                    + obj.UCity
                    + "\t"
                )

    def showAdmin():
        for obj in MuserDL.muserList:
            if obj.Role == "User":
                print(
                    obj.Uid
                    + "\t"
                    + obj.fName
                    + "\t"
                    + obj.LoginName
                    + "\t"
                    + obj.LoginPassWord
                    + "\t"
                    + obj.Role
                    + "\t"
                    + obj.UGender
                    + "\t"
                    + obj.UCity
                    + "\t"
                )

    def PriviousRecord():
        UI.clearScreen()
