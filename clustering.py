import os
import math
import numpy as np

# kmeans clustering algorithm
# data = set of data points
# k = number of clusters
# c = initial list of centroids (if provided)
#
def kmeans(data, k, c):
    centroids = []

    centroids = init_centroids(data, centroids, k)  

    old_centroids = [[] for i in range(k)] 

    iterations = 0
    result = [[] for i in range(k)]

    while not (has_converged(centroids, old_centroids, iterations)):
        iterations += 1

        clusters = [[] for i in range(k)]

        # assign data points to clusters
        clusters = euclidean_dist(data, centroids, clusters, k)

        # recalculate centroids
        index = 0
        for cluster in clusters:
            old_centroids[index] = centroids[index]
            centroids[index] = min(cluster, key=lambda t:t[2])
            index += 1

    #print("The total number of data instances is: " + str(len(data)))
    #print("The total number of iterations necessary is: " + str(iterations))
    #print("The means of each cluster are: " + str(centroids))
    #print("The clusters are as follows:")
    #for cluster in clusters:
     #   print("Cluster with a size of " + str(len(cluster)) + " starts here:")
     #   print(np.array(cluster).tolist())
     #   print("Cluster ends here.")

    return clusters

# Calculates euclidean distance between
# a data point and all the available cluster
# centroids.
def unbalanced (data, k, cluster):
    return (len(cluster) > (len(data)/k+1))

def dist(a,b,c,):
    if c :
        return 500
	x = a[0]-b[0]
	y = a[1]-b[1]
	return math.sqrt(x*x+y*y)

def euclidean_dist(data, centroids, clusters, k):
    for instance in data:  
        # Find which centroid is the closest
        # to the given data point.
        mu_index = min([(i[0], dist(instance,centroids[i[0]],unbalanced(data,k,clusters[i[0]]))) \
                        for i in enumerate(centroids)], key=lambda t:t[1])
        try:
            clusters[mu_index[0]].append(instance)
        except KeyError:
            clusters[mu_index[0]] = [instance]

    # If any cluster is empty then assign one point
    # from data set randomly so as to not have empty
    # clusters and 0 means.        
    for cluster in clusters:
        if not cluster:
            cluster.append(data[np.random.randint(0, len(data), size=1)])

    return clusters


# randomize initial centroids
def init_centroids(data, centroids, k):
    for cluster in range(0, k):
        centroids.append(data[1])
    return centroids


# check if clusters have converged    
def has_converged(centroids, old_centroids, iterations):
    MAX_ITERATIONS = 1000
    if iterations > MAX_ITERATIONS:
        return True
    return old_centroids == centroids