import os
import one

list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    12,
    12,
    23,
    34,
    4,
    56,
    67,
    34,
    324,
    65,
    34,
    23,
    543,
    23,
    54,
    23,
    75,
    545,
]
name = "Amad Irfan"

newName = one.subString(name, 0, 4)

# sets=(1,1,3,4,5,23,1,3,4,2,4,5,6,7,24,)
# t=tuple(sets)
# s=set(sets)
# print(s)
# print(t)
# print(type(s))
# print(type(t))

qList = [
    {
        "question": "what is your name",
        "answer": [
            {
                "answer": "Amad",
                "score": 12,
            },
            {
                "answer": "Saad",
                "score": 10,
            },
            {
                "answer": "Jawad",
                "score": 8,
            },
            {
                "answer": "Amad",
                "score": 16,
            },
        ],
    },
    {
        "question": "what is your Father Name ? ",
        "answer": [
            {
                "answer": "Irfan",
                "score": 12,
            },
            {
                "answer": "Tariq",
                "score": 10,
            },
            {
                "answer": "Akhter",
                "score": 8,
            },
            {
                "answer": "Nasir",
                "score": 16,
            },
        ],
    },
]


def clearScreen():
    print('Press any key to continue : ')
    os.system('cls')
    one.TopBar("Quiz")

def menu():
    print("\n\n\n")
    print("1).\t Start Quiz")
    print("2).\t Exit")
    print('-----------------')
    menuNumber = input("\n\t Input : ")
    
    return menuNumber


def main():
    num = "0"
    while num != "2":
        num = menu()
        if num == "1":
            print("start quiz")
        elif num == "2":
            print("exit")
            break


if __name__ == "__main__":
    main()
