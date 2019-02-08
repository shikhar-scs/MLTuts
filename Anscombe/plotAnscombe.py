import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
set_1 = data.loc[data.dataset == 'I'].iloc[:,2:4]
set_2 = data.loc[data.dataset == 'II'].iloc[:,2:4]
set_3 = data.loc[data.dataset == 'III'].iloc[:,2:4]
set_4 = data.loc[data.dataset == 'IV'].iloc[:,2:4]

def linear_regression(set):
    x_mean = set.x.mean()
    y_mean = set.y.mean()
    yi = sum([(x-x_mean)*(y-y_mean) for x,y in zip(set.x, set.y)])
    xi = sum([(x-x_mean)*(x-x_mean) for x in set.x])
    slope = yi/xi
    con = y_mean-x_mean*slope
    plot_graph(slope, con, set)

def plot_graph(slope, con, set):
    x = np.linspace(-1,15,200)
    y = slope*x+con
    plt.plot(x, y, '-r', label='Equation')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.scatter(set.x, set.y)
    plt.show()

linear_regression(set_1)
linear_regression(set_2)
linear_regression(set_3)
linear_regression(set_4)