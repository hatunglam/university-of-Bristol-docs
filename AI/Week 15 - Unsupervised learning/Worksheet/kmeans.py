import numpy as np
import matplotlib.pyplot as plt

class KMeans:

    def __init__(self, k= 3): 
        self.k = k
        self.centroids = None

    def l2_dist(datapoint, centroid):
        return np.sqrt(np.sum((centroid - datapoint)**2, axis= 1))

    def fit(self, X, max_iter= 200):
        self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis= 0),
                                           size= (self.k, X.shape[1]))

        for _ in range(max_iter):
            y = []

            for data in X:
                dist = KMeans.l2_dist(data, self.centroids)
                cluster_num = np.argmin(dist)
                y.append(cluster_num)

            y = np.array(y)

            cluster_i =  []

            for i in range(self.k): 
                cluster_i.append(np.argwhere(y == i))

            cluster_center = []

            for i, indices in enumerate(cluster_i):
                if len(indices) == 0:
                    cluster_center.append(self.centroids[i])
                else:
                    cluster_center.append(np.mean(X[indices], axis=0)[0])

            if np.max(self.centroids - np.array(cluster_center)) < 0.0001:
                break
            else:
                self.centroids = np.array(cluster_center)

        return y




      