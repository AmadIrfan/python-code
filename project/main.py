from UI import UI
from MuserDL import MuserDL
from Muser import Muser
from customerDL import customerDL
from adminUI import AdminUI
from userUI import UserUI
from carsDL import carsDL
from carsUI import CarsUI
from cars import cars
from os import system


def main():
    true = True
    inputVar = "0"
    while true:
        UI.clearScreen()
        inputVar = UI.MainMenu()
        if inputVar == "4" or inputVar == "3" or inputVar == "2" or inputVar == "1":
            UI.clearScreen()
            if inputVar == "1":
                UserInput = "0"
                userTrue = True
                while userTrue:
                    UserInput = UserUI.userMenu()
                    if UserInput == "1" or UserInput == "2" or UserInput == "3":
                        UI.clearScreen()
                        if UserInput == "1":
                            user = "0"
                            ExUserTrue = True
                            while ExUserTrue:
                                user = UserUI.existing_user_manu()
                                if (
                                    user == "1"
                                    or user == "2"
                                    or user == "3"
                                    or user == "4"
                                ):
                                    UI.clearScreen()
                                    if user == "1":
                                        CarsUI.ShowCars()
                                    if user == "2":
                                        CarsUI.BookCars()
                                    if user == "3":
                                        UserUI.PriviousRecord()
                                    if user == "4":
                                        ExUserTrue = False
                                        break
                                else:
                                    user = UI.WrongInput()
                        if UserInput == "2":
                            UI.clearScreen()
                            temp = UserUI.newcustomer()
                            MuserDL.addMuserIntoList(temp)
                        if UserInput == "3":
                            userTrue = False
                            break
                    else:
                        UserInput = UI.WrongInput()
            if inputVar == "2":
                UI.clearScreen()
                adminTrue = True
                adminInput = "0"
                while adminTrue:
                    adminInput = AdminUI.adminMenu()
                    if (
                        adminInput == "1"
                        or adminInput == "2"
                        or adminInput == "3"
                        or adminInput == "4"
                        or adminInput == "5"
                        or adminInput == "6"
                        or adminInput == "7"
                    ):
                        if adminInput == "1":
                            UI.clearScreen()
                            Admin = AdminUI.addAdmin()
                            MuserDL.addMuserIntoList(Admin)
                        if adminInput == "2":
                            UI.clearScreen()
                            car = CarsUI.addCars()
                            carsDL.addCarsIntoList(car)
                        # if adminInput == "3":
                        if adminInput == "4":
                            user.showAdmin()
                            user.showUser()
                        if adminInput == "5":
                            UI.clearScreen()
                            CarsUI.ShowCars()
                        # if adminInput == "6":
                        if adminInput == "7":
                            adminTrue = False
                            break
                    else:
                        adminInput = UI.WrongInput()
            if inputVar == "3":
                UI.clearScreen()
                UI.tearmsCondition()
            if inputVar == "4":
                true = False
                break
        else:
            inputVar = UI.WrongInput()


if __name__ == "__main__":    
     main()

