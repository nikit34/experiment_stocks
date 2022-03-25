import sys

import pandas as pd
import matplotlib.pyplot as plt


if len(sys.argv) != 3:
    print('You need to run script with two arguments: names of files to analyze')
    sys.exit()

stockA = pd.read_csv(sys.argv[1])
stockB = pd.read_csv(sys.argv[2])

def get_average_drop(df, columns):
    df['Average'] = 0
    for column in columns:
        df['Average'] += df[column]
        df = df.drop(column, axis=1)
    df['Average'] /= 4
    return df

stockA = get_average_drop(stockA, ['Open', 'High', 'Low', 'Close', 'Adj Close'])
stockB = get_average_drop(stockB, ['Open', 'High', 'Low', 'Close', 'Adj Close'])

def get_absolute_buy(df):
    df['Absolute'] = df['Volume'] * df['Average']
    return df

stockA = get_absolute_buy(stockA)
stockB = get_absolute_buy(stockB)

plt.figure(figsize=(18, 16), dpi=80)
plt.plot(stockA['Absolute'], 'g')
plt.plot(stockB['Absolute'], 'b')
plt.show()