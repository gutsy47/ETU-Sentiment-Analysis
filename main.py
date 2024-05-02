import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("negative.csv")
    df2 = pd.read_csv("positive.csv")
    print(df.iloc[:, 3])
    print(df2.iloc[:, 3])
