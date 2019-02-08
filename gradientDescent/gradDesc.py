from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def step_gradient(b_current, m_current, points, learningRate):
    N = float(len(points))
    b_gradient = sum([-(2/N) * (y - ((m_current * x) + b_current)) for x,y in zip(points[:,0],points[:,1])])
    m_gradient = sum([-(2/N) * x * (y - ((m_current * x) + b_current)) for x,y in zip(points[:,0],points[:,1])])
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def plot_graph(slope, con):
    x = np.linspace(-1,90,1000)
    y = slope*x+con
    plt.plot(x, y, '-r', label='')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.pause(0.05)

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
        plt.scatter(points[:, 0], points[:, 1])
        plot_graph(m,b)
        plt.clf()
    plt.show()

points = genfromtxt("data.csv", delimiter=",")
learning_rate = 0.000001
initial_b = 0
initial_m = 0
num_iterations = 1000
gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
