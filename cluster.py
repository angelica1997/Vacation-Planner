import json
from cluster import KMeansClustering

attracs = [(1,0),(0,1),(10,10),(11,11),(-10,-10),(-11,-11)]

cl = KMeansClustering(attracs)
clusters = cl.getclusters(3)

print clusters
