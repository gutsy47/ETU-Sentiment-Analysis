import pandas as pd


if __name__ == '__main__':
    headers = ["text", "label"]

    df_positive = pd.read_csv("positive.csv", usecols=[3], header=None)
    df_positive["label"] = 1

    df_negative = pd.read_csv("negative.csv", usecols=[3], header=None)
    df_negative["label"] = 0

    df_concat = pd.concat([df_positive, df_negative], ignore_index=True)
    df_concat.columns = headers

    print(df_concat)

    df_concat.to_csv("data.csv", index=False)
