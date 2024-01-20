from operator import index
from UI import UI
from carsDL import carsDL
from cars import cars


class CarsUI:
    def addCars():
        carBrandName = input("Enter brand name ")
        carColor = input("Enter ar colour ")
        carModel = input("Enter car model ")
        carPlateNumber = input("Enter car number plate ")
        carRpd = input("Enter rate per days")
        carStatus = input("Enter Car status ")
        carConditions = input("Enter car conditions ")
        NewCar = cars(
            carBrandName,
            carColor,
            carModel,
            carPlateNumber,
            carRpd,
            carStatus,
            carConditions,
        )
        return NewCar

    def ShowCars():
        print("ME AMAD IRFAN")
        for obj in carsDL.carsList:
            print(
                obj.carBrandName
                + ","
                + obj.carColor
                + ","
                + obj.carModel
                + ","
                + obj.carPlateNumber
                + ","
                + obj.carRpd
                + ","
                + obj.carStatus
                + ","
                + obj.carConditions,
            )

    def BookCars():
        day = 0
        totalPayment = 0
        print(
            "Sr.No \t brand_name \t Color \t model \t number Plate \t status \t RPD \t condition"
        )
        CarsUI.ShowCars()
        press = input(
            "                   are you sure to book car\n           Press (y/Y)to Book a car \n         Press (N/n) to cancal Booking"
        )
        if press == "y" or press == "Y":
            No = input("    Enter Sr.no to continue.... ")
            if carsDL.carsList[No].carStatus == "Booked":
                print(
                    "Your selected car is already booked please choose another cars..."
                )
            else:
                print(
                    "Sr.No \t brand_name \t Color \t model \t number Plate \t status \t RPD \t condition"
                )
                for obj in No:
                    print(
                        index
                        + "\t"
                        + obj.carbrandName
                        + +"\t"
                        + obj.carColor
                        + "\t"
                        + obj.carModel
                        + "\t"
                        + obj.carPlateNumber
                        + "\t"
                        + obj.carStatus
                        + "\t"
                        + obj.carRpd
                        + "\t"
                        + obj.carConditions
                        + "\t"
                    )
                    day = input("Enter number of days you want to enter ")
                    totalPayment = day * obj.carRpd
                print(
                    "You have to pay total "
                    + totalPayment
                    + "/- rupees for booking this car "
                )
        elif press == "N" or press == "n":
            print("                 Thank you ! to choose our servise..")
            UI.clearScreen()
