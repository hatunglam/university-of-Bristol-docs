import numpy as np

class K_Means:
    def __init__(self, k=3, tol= 0.001, max_iter= 300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = X[i] 

        for i in range(self.max_iter):
            self.classification = {}

            for i in range(self.k):
                self.classification[i] = []

            for featureset in X:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroid = dict(self.centroids)
            
            for classification in self.classification:
                pass
                c=self.centroids[classification] = np.average(self.classification[classification], axes= 0)
                
        
        pass

    def predict(self, X):
        pass