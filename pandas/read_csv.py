import pandas as pd


def readCsv():
    r = pd.read_csv("rData.csv")
    # a = r.columns
    # a = r.index
    # a=r.index.array
    # print(r.describe())
    # print(r[10:20])
    # print(r.head(10))
    # a=pd.Series()
    # a=r.columns
    # print(a)
    # print(a)
    # print(r.to_markdown)
    # print(r.sort_index(ascending=False,axis=1))
    r['Year'][0]='20211'
    # print(r);
    q=r.loc[[1,10],['Year','Value']]
    q=r.loc[:,['Year','Value']]
    q=r.loc[[1,10],:]
    q=r.iloc[0,1]
    print(q)


readCsv()
