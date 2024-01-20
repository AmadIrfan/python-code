
num=int(input("Enter a number "))

i=0
mod =0
while(num>0):
    mod=num%10
    i=i+mod
    num=num//10
    print(num,i)
print(i)