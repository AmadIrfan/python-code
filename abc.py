import os as o
import random


def viruse(name,num):
    for i in range(1,num):
        file=open('{}\'s {}.txt'.format(name,i),"w")
        file.write('your name is  {} and you dont\' know me '.format(name))
        file.close()



if __name__=="__main__":
    name=input('Enter your name ')
    num=input('enter the number you want to enter ')
    viruse(name,int(num))