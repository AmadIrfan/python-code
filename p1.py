
def main():
    set=(1,4,2,5,5,7,2,7,9,10)
    print(set)
    dict={"amad":'2021','saad':'2020','jawad':'2019','tariq':{1:"a",2:"s",3:"d",4:"f",5:"g",6:"h",}}
    print(dict["tariq"][1])
    del dict['tariq']
    print(dict.keys())
    print(dict.values())
    print(dict.update({'khan':123}))
    print(dict)






if __name__=="__main__":
    main()