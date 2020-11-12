# -*- coding: utf-8 -*-
#
import util

# import helper

NO_NAME_PRINT = True

# Sample class
class Sample(object):
    """
    each instance of the Sample class is one data point in the k-means problem
    """
    def __init__(self, name, features, label = None):
        #Assumes features is an array of numbers
        """for the 2-d k-means prob, features are the x, y coordinates
        stores in a list [x, y] """
        self.name = name
        self.features = features
        self.label = label  # for group info?

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        return util.minkowskiDist(self.features, other.getFeatures(), 2)

    def setLabel(self, new_label):
        self.label = new_label

    def setName(self, new_name):
        self.label = new_name

    def __add__(self, other):
        """ other is another Sample instance"""
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+', f, self.label)

    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f, self.label)

    #### Implement an overwrite of the '-' operator here!
    def __sub__(self, other):
        ''' replace the line below with you code
            refer to the __add__ for ideas '''
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] - other.getFeatures()[i])
        return Sample(self.name + '-', f, self.label)
    #
    def __mul__(self, other):
        ''' bonus: can you do vector multiplication?
            this is two vectors element-wise multiplication '''
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] * other.getFeatures()[i])
        return Sample(self.name + '*', f, self.label)


    def power(self, x):
        ''' replace the line below with you code
            refer to the __add__ for ideas '''
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] ** x)
        return Sample(self.name + '^', f, self.label)
    #
    def vec_div(self, other):
        ''' replace the line below with you code
            refer to the __add__ for ideas '''
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] / float(other.getFeatures()[i]))
        return Sample(self.name + '/', f, self.label)

    def __str__(self):
        if NO_NAME_PRINT:
            return str(self.features)
        else:
            return self.name +' : '+ str(self.features) + ' : ' + str(self.label)

if __name__ == "__main__":
    a = Sample('a', [1, 1])
    b = Sample('b', [-1, -1])
    c = Sample('c', [10, 10])
    print(a)
    print(b)
    print(a + b)
    print(c - a - b)
    print(a / 2)
    print(a * b)
    print(b.power(2))
    print(a.vec_div(b))
    print(a.dimensionality())
    print(a.getFeatures())
    print(a.distance(b))
