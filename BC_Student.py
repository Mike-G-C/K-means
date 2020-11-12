import random
import util
import cluster_student as cluster
# import helper
import sample_student as sample

from kmeans_student import *


# Kmeans: take a list of samples and make k clusters


def kmeansTest(k=2, n=20, verbose=False):
    random.seed(0)

    """read the data from BC_data.csv
    create a dataset 'allSamples' which contains all data point
    Use the first column 'id' as index
    Use the second column 'diagnosis' as label,
    Use 'radius_mean'  and 'texture_mean' as features
    """




    l = open("BC_data.csv").readlines()[1:]
    data = [[i for i in line.strip().split(',')] for line in l]

    allSamples = [sample.Sample(i[0], [float(j) for j in i[2:4]], i[1]) for i in data]


    print("before clustering")
    util.plot_cluster([cluster.Cluster(allSamples)])

    # plot the data from the two groups "B" and "M"
    cluster_b = [s for s in allSamples if s.getLabel() == 'B']
    cluster_m = [s for s in allSamples if s.getLabel() == 'M']
    clusters = [cluster.Cluster(cluster_b), cluster.Cluster(cluster_m)]
    print("clustering with label info")
    util.plot_cluster(clusters)

    # Perform cluster analysis with k=2 and plot the clusters
    print("after clustering")
    """Implement cluster analysis here
    """





    clusters = kmeans(allSamples, k, verbose)

    util.plot_cluster(clusters, verbose)

    print('Final result')
    for c in clusters:
        print('', c)


if __name__ == "__main__":
    random.seed(0)
    kmeansTest(k=2)
