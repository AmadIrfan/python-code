class Employee:
    def __init__(self, id, fName, lName, phone):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.phone = phone
        print(
            str(self.id) + "," + self.fName + "," + self.lName + "," + self.phone + ","
        )

    # @classmethod
    def employeeEmail(self):
        email = self.fName + "." + self.lName + "@gmail.com"
        return email

    def employeePhoneNo(self):
        return self.phone

    def toFile(self):
        file = open("employee.txt", mode="a")
        file.writelines(
            str(self.id)
            + ","
            + self.fName
            + ","
            + self.lName
            + ","
            + self.phone
            + ",\n"
        )
        file.close()
        file1 = open("employeeData.txt", mode="a")
        file1.writelines(
            str(self.id)
            + ","
            + self.employeeEmail()
            + ","
            + self.employeePhoneNo()
            + ",\n",
        )
        file1.close()
        return

    @staticmethod
    def fromFile():
        list = []
        file = open("employee.txt", mode="r")
        r = file.read()
        # return r


emp1 = Employee(1233433, "Ai", "khan", "03460151920")

# print(emp1)
# print(emp1.employeePhoneNo())
# print(emp1.employeeEmail())
# emp1.toFile()

print(Employee.fromFile())
