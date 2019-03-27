import pandas as pd
import math

def find_entropy(ent_data):
    yes_data = len(ent_data.loc[ent_data.play == 'yes'])
    no_data = len(ent_data.loc[ent_data.play == 'no'])
    total = yes_data+no_data
    no_data = total if no_data == 0 else no_data
    yes_data = total if yes_data == 0 else yes_data
    return -(yes_data/total*(math.log(yes_data/total)) + no_data/total*(math.log(no_data/total)))/math.log(2)

def find_gain(gain_data, attr):
        attr_gain_val = [find_entropy(gain_data.loc[gain_data.iloc[:, 0] == att]) for att in attr]
        attr_gain_len = [len(gain_data.loc[gain_data.iloc[:, 0] == att]) for att in attr]
        return sum([x*y/sum(attr_gain_len) for x,y in zip(attr_gain_len,attr_gain_val)])

def id3(dataset, level, col):
    attributes = []
    attributes.append([dataset[dataset.columns[i]].unique() for i in range(col - 1)])
    gain_val = [0, 0, 'a']

    for i, attribute in enumerate(attributes[0]):
        temp_data = dataset.iloc[:,(i,col-1)]
        gain_s_a = find_entropy(temp_data)-find_gain(temp_data, attribute)
        if gain_val[0] <= gain_s_a:
            gain_val = [gain_s_a, i, dataset.columns[i]]
    if gain_val[0] == 0:
        fin_values.append([level, dataset.iloc[:,col-1].unique(), 'decision'])
        return
    for att in attributes[0][gain_val[1]]:
        fin_values.append([level, gain_val, att])
        new_data = dataset.loc[(dataset.iloc[:, gain_val[1]] == att)].drop(gain_val[2], axis=1)
        id3(new_data, level+1, new_data.shape[1])

data = pd.read_csv('play_tennis.csv')
fin_values = []
id3(data,0, data.shape[1])
level_texts = [None]*(data.shape[1])

for i in range(len(fin_values)):
    if fin_values[i][2] == 'decision':
        level_texts = [x for x in level_texts if x is not None]
        print('if ' + ' '.join(level_texts)[:-4] + 'then play is ' + fin_values[i][1][0].upper())
        continue
    level_texts[fin_values[i][0]:] = [None]*(data.shape[1]-fin_values[i][0])
    level_texts[fin_values[i][0]] = fin_values[i][1][2].upper() + ' is ' + fin_values[i][2].upper() + ' and '