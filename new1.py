def main():
    number=18
    gussNo=4
    while(True):
        value=input('Gusse a number and you try {0} more time '.format(gussNo))
        gussNo=gussNo-1
        print(gussNo)
        if(value==number or gussNo>0):
            print('You won and remaining trys are {0}'.format(gussNo))
            break
        elif(value!=number & gussNo==0):
            print("You failed")
            break


if __name__=="__main__":
    main()