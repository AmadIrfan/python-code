from os import system


def main():
    for i in range(20):
        print('amadirfan')
        

def menu():
    print('-------------------------');
    print('-------------------------');
    print('----------menu-----------')
    print('-------------------------');
    print('-------------------------');
    print('1). Login');
    print('2). Register');
    print('3). Exit.');
    print('\n\n-------------------------');
    inp=input('Enter value :   ')
    

    return inp;






def checkValidInput(value):
    if(int(value)>=1 and int(value) <=3 ):
        return value;
    else:
        print('in valid input ..... ')
        input('press any key to continue .....');
        menu()


    




























if __name__== '__main__':
    # print('this is main calling method')
    # main()
    val=menu()
    checkValidInput(val)
    

