#coding=UTF-8

from __future__ import division
from math import log
from collections import *

def createDTree():
    pass

def selDataset(dataSet, selCol, selValue):
    newdataSet = []
    for dataRow in dataSet:
        if dataRow[selCol] == selValue:
            head = dataRow[:selCol]
            head.extend(dataRow[selCol + 1:])
            newdataSet.append(head)
    return newdataSet

def calcEntropy(dataSet):
    n = len(dataSet)
    entropy = 0.0
    dataDict = Counter(dataSet)
    for c in dataDict.itervalues():
        p = c / n
        entropy -= p * log(p, 2)
    return entropy

if __name__ == '__main__':
    print calcEntropy([1,1,2,2])
    print selDataset([[1,2,'yes'],[1,1,'yes'],[0,2,'no']], 0, 1)