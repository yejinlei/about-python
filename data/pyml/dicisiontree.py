#coding=UTF-8

from __future__ import division
from math import log
from collections import *

def calcEntropy(dataset):
    n = len(dataset)
    entropy = 0.0
    datadict = Counter(dataset)
    for c in datadict.itervalues():
        p = c / n
        entropy -= p * log(p, 2)
    return entropy

if __name__ == '__main__':
    print calcEntropy([1,1,2,2])