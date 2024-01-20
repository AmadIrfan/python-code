import random as rd


class Students:
    def __init__(self, name, section, session, age):
        self.id = rd.randint(0, 300)
        self.name = name
        self.age = age
        self.section = section
        self.session = session
        print(self.id, name, age, section, session)

    @classmethod
    def getStudentRegNo(cls, text: str):
        name, age, section, session = text.split("-")
        a = cls(name, age, section, session)
        print(cls.studentEmail(self=a))
        # return str(self.session) + "-" + self.section + "-" + str(self.id)

    def studentEmail(self):
        return str(self.session) + self.section + str(self.id) + "@gmail.com"

class University(Students):
    name=''
    def __init__(self, name, section, session, age,uniName):
        super().__init__(name, section, session, age)
        self.name=uniName
        print(self.name)


stu1 = University("AmadIrfan", "CS", 2021, 22,uniName='UET')
# stu1.getStudentRegNo(text="amadirfan-20-cs-2021")
