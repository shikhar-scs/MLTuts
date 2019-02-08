import pandas as pd

dataset = pd.read_csv('data.csv')

def checkUnique(row):
    for i in range(len(row)):
        if row[i] == 1:
            fin.append(data[data.columns[i]].iloc[0])
        else:
            fin.append('?')
    return fin

for i in range(1,8):
    fin = []
    data = dataset.loc[dataset.type == i].iloc[1:, :17]
    print(checkUnique([len(data[data.columns[i]].unique()) for i in range(data.shape[1])]))