import pandas as pd

# a = {
#     "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
#     "data1": [11, 22, 33, 44, 55, 66, 77, 88, 99, 00],
# }

# pf = pd.DataFrame(a)
# print(pf.head(3))
# print(pf.tail())
# print(pf.head())
# print(pf)
# print(pf)

# data = {
#     "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
#     "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
#     "MaxPulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
#     "Calories": {"0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300},
# }

# pf = pd.DataFrame(data)
# pf.to_csv("data.csv",index=False)

pf = pd.read_csv("data.csv")
# data=pf.to_json()
# print(pf.head())
# print(pf.tail())
pf.dropna(inplace=True)
x=pf.mean()
print(x)
pf.fillna(0,inplace=True)
# print(pf['Year'])
# print(pf['Year'][10])
print(pf)
