import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(len(data)):
        currentItem = data[i]
        for j in range(len(data)):
            if i == j:
                dist[i][j] = np.inf
            else:
                localDist = 0
                for k in range(len(data[i])):
                    localDist = localDist + abs(data[i][k] - data[j][k])
                dist[i][j] = localDist
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)