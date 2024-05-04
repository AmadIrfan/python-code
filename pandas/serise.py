import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": [12, 2312]}

# myvar = pd.Series(calories)
# print(myvar)
#
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
