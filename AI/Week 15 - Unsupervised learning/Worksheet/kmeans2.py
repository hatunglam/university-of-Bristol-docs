import numpy as np

class KMeans:

    def __init__(self, k=5, max_iter= 100, plot_step= False):
        self.k = k
        self.max_iter = max_iter
        self.plot_step = plot_step

        # List of sample indices for each cluster
        self.cluster = [[] for _ in range(self.k)]

        # Center
        self.centroids = []

    def fit(self, X):
        self.X = X
        self.n_samples, self.n_feature = X.shape

        # Init centroid
        random_sample_id = np.random.choice(self.n_samples, self.K, replace = False)
        self.centroids = [self.X[idx] for idx in random_sample_id]

        #optimize cluster
        for _ in range(self.max_iter):
            # assign samples to the closest centroid
            self.cluster = self._create_cluster(self.centroids)

            if self.plot_step:
                self.plot()

            # Calculate new centroid
            centroid_old = self.centroids
            self.centroids = self._get_centroid(self.cluster) 

            if self._is_converged(centroid_old, self.centroids):
                break

            if self.plot_step:
                self.plot()

        # Classify samples as the index of cluster
        return self._get_cluster_label(self.cluster)

    def _create_cluster(self, centroid):
        # Assign the sample to the closest centroid
        cluster = [[] for _ in range(self.k)]
        for i, sample in enumerate(self.X)

        pass

    def _closest_centroid(self, sample, centroid):
        # distance of the current sample to each centroid
        distances = [euclidean_distance(sample, point) for point in centroid]
        closest_id = np.argmin(distances)
        return closest_id

    def _get_centroid(self, cluster):
        pass 

    def _is_converged(self, centroid_old, centroid):
        pass

    def _get_cluster_label(self, cluster):
        # Each sample will get the label of the cluster it was assigned to
        label = np.empty(self.n_samples)
        for i, cluster in enumerate(cluster):
            for index in cluster:
                label[index] = i

        return label     

    def plot(self);
        pass