class mUser:
    name = ""
    password = ""
    Role = ""

    def __init__(self, *Pass):
        self.Role = Pass

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.Role = role


class mUserDl:
    userList = []

    def AddUserIntoList(Temp):
        mUserDl.userList.append(Temp)


def main():
    option = 0
    while option <= 3:
        print("(1).lOGIN\t\n(2).SignUp\t\n(3).Exit")
        option = int(input("Your Choice "))
        if option == 1:
            Login()
        if option == 2:
            SignUp()
        if option == 3:
            break


def Login():
    role = ""
    name = input("Enter your name ")
    print(name)
    password = input("Enter your password ")
    print(password)
    for obj in mUserDl.userList:
        print(name + "," + password)
        print(obj.name + "," + obj.Role + "," + obj.password)
        if name == obj.name and password == obj.password:
            role = obj.Role
            print(role)
    if role == "admin":
        for obj1 in mUserDl.userList:
            print(obj1.name + "\t" + obj1.password + "\t" + obj1.Role)


def SignUp():
    name = input("Enter your name ")
    password = input("Enter your password ")
    role = input("Enter your Role ")
    user = mUser(name, password, role)
    mUserDl.AddUserIntoList(user)


if __name__ == "__main__":
    main()
