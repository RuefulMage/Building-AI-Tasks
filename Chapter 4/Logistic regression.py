import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i] * z[i]
    s = 1 / (1 + math.exp(-sum))
    print(s)

sigmoid(c1)
sigmoid(c2)
sigmoid(c3)
# calculate the output of the sigmoid for x with all three coefficients

