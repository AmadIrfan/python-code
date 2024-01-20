# class
class student:
    name="NA"
    matricMarks=24.0
    fscMarks=55.0
    ecatMarks=34.0
    merit=0.0
    # function
    def calculateMerit(self):
        merit=((0.25*self.matricMarks/1100)+(0.45*self.fscMarks/1100)+(0.3*self.ecatMarks/400))
        return merit

    # constructor
    def __init__(self,name,matricmarks,fscmarks,ecatmarks):
        self.name=name
        self.matricMarks=matricmarks
        self.fscMarks=fscmarks
        self.ecatMarks=ecatmarks
    def showInfo(self):
        print("My name is ",self.name," Matric Marks ",self.matricMarks," Fsc Marks ",self.fscMarks," Ecat Marks ",self.ecatMarks)


# variable declerations..........
x=6
y=7
t=x+y
x=input("enter your name: ")
# condition statements
if(x=="A"):
    print("Welcome  "+x)
    print("NUmber  ",x)
else:
    print("GoodBye "+x)
print("t="+str(t))
# for loop
for i in(1,2,3,4,5):
    print("i="+str(i))
for i in range(1,6,2):
    print("i="+str(i))
# while loop
i=1
while i!=3:
    i=int(input("Enter Number: "))
    # check type of variable
    print(type(i))
print("Loop End")
# array
num=range(0,10)
for i in range(0,10):
    print(num[i])
# function
def add(a,b):
    return a+b
# import for file handling
import os.path
# main function
def main():
    x=add(2,4)
    print("x=",x)
    # object decleration
    s=student()
    # using object
    s.name=input("Enter Name ")
    s.ecatMarks=int(input("Enter Ecat Marks "))
    s.fscMarks=int(input("Enter Fsc Marks "))
    s.matricMarks=int(input("Enter Matric Marks "))
    s.showInfo()
    # file handling
    if(os.path.exists("data.txt")):
        f=open("data.txt","r")

# main calling
if __name__ == "__main__":
    main()

