
A=[5,9,2,4,6,1,3,2]


for i in range(1,len(A)): # 
    key=A[i]
    j=i-1
    a=A[j]
    while j>=0 and A[j]>key:
        A[j+1]=A[j]
        j=j-1
        A[j+1]=key
print(A)