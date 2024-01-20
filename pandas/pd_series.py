import pandas as pd
import random as r


def pd_Series():
    x = [1, 2, 3, 10, 4, 5, 6, 7, 9, 8]
    y = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l"]
    z = [1, 2, 3, 10, 4, 5, 6, 7]
    x1 = {
        "a": [23, 1, 4, 23, 223, 123, 32],
        "b": [123, 32],
        "c": [23, 1, 4, 23, 223],
    }

    # r = pd.Series(data=y ,name="my Random Data", index=y, copy=True )
    # r = pd.Series(data=x, dtype=float)
    # r=pd.Series(data=12,dtype=float,index=y)
    r = pd.Series(x1)
    # r1 = pd.Series(y)
    r.to_csv('my_series.csv')
    print(r)
    print(type(r))


pd_Series();



# def getRandomData():
#     for i in range(0, 1000):
#         a = r.randint(0, 1000)
#         x.append(a)
# getRandomData()
