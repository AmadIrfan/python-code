import pandas as pd
import time as t
import os

os.system("cls")


class Person:
    def __init__(self, name):
        self.name = name
        self.one = name[0:2]

    # def showDetails(self):
    #     print(self.name)
    #     print(self.one)

    def loop(self, s, e):
        list = []
        for i in range(s, e):
            list.append(i)
        return list

    def toFileUsingIo(self, s, e):
        list = []
        sTime = t.time()
        f = open("exl1.csv", mode="w")
        for i in range(s, e):
            f.write(str(i))
            list.append(i)
        f.close()
        eTime = t.time()
        tTime = eTime - sTime
        print("io time taking {0}".format(tTime))

        # pf = pd.DataFrame({"Numbers ": list})
        # pf.to_csv("exl.csv", index=False, encoding="utf-8")

    @staticmethod
    def toFile(s, e):
        sTime = t.time()
        a = Person("amad")
        list = a.loop(s, e)
        pf = pd.DataFrame({"Numbers ": list})
        pf.to_csv("exl.csv", index=False, encoding="utf-8")
        eTime = t.time()
        tTime = eTime - sTime
        print("csv time taking {0}".format(tTime))


obj = Person("Amad Irfan")

obj.toFileUsingIo(0, 30000)
obj.toFile(0, 30000)
