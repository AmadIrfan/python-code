class Employee:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age

    def printEmail(self):
        print(self.name + "gmail.com")


class Boss(Employee):
    def __init__(self, name, age, id, employee):
        super().__init__(name, age, id)
        if employee is not None:
            print(employee)
        else:
            print("None")


employee = Employee("amad", age=20, id=213123213123123)
employee1 = Boss(name="amad", age=20, id=213123213123123, employee=[employee])
employee2 = Boss(name="amad", age=20, id=213123213123123)

# employee.printEmail()
print(67 - 25)
