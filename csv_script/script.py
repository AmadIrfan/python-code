import pandas as pd

df = pd.DataFrame(
    {
        "text": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        "text1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    }
)
df.to_csv("my.csv", index=False,mode='a')

df1 = pd.DataFrame(
    {
        "text": "2324234",
    }
)

df1.to_csv("my.csv", index=False,mode='a')
