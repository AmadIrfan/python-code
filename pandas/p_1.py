import pandas as pd

""" 

myDataSet = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]

}
list=[1,2,2]
# print(pandas.DataFrame(list))
# print(type(myDataSet))

# myvar = pandas.DataFrame(myDataSet)
# print(myvar)

a=pd.Series(list,index=['x','y','z'])
# print(a)
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

# print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar) """

a = [
    1,
    2,
    4,
    5,
    6,
    7,
    98,
    0,
    2,
    2,
    324,
    23423,
]

pf = pd.DataFrame(a)
print(
    pf,
)

data = {
    "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
    "MaxPulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
    "Calories": {"0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300},
}

pf = pd.DataFrame(data)
print(pf)
