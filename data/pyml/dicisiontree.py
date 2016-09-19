#coding=UTF-8

from __future__ import division
from math import log
from collections import *

def createDTree():
    pass

def splitFeatureFromSet(dataSet, selCol, selValue):
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
    #Counter用于统计元素的频率，但无法统计[list,list，...]
    dataDict = Counter([str(row) for row in dataSet])
    for c in dataDict.itervalues():
        p = c / n
        entropy -= p * log(p, 2)
    return entropy

def chooseBestFeature(dataSet):
    #数据集中携带分类信息
    numFeature = len(dataSet[0]) - 1
    #计算总的熵
    allEntropy = calcEntropy(dataSet)
    infoGainSet = []
    colSet = []
    for col in range(numFeature):
        #默认最后一列为非特征，选取一列特征值集合
        curFeature = [feature[col] for feature in dataSet]
        #从特征值集合中，过滤重复项，即特征分类
        curFeatureClass = set(curFeature)

        #计算条件熵，从集合中删除本特征后得到的熵
        condEntropy = 0.0
        for featureValue in curFeatureClass:
            newdataSet = splitFeatureFromSet(dataSet, col, featureValue)
            p = len(newdataSet) / len(dataSet)
            condEntropy += p * calcEntropy(newdataSet)
        infoGain = allEntropy - condEntropy
        infoGainSet.append(infoGain)
    infoGainDict = {i:infoGain for i, infoGain in enumerate(infoGainSet)}
    infoGainDict = sorted(infoGainDict.iteritems(), key=lambda d:d[1], reverse = True)
    return  infoGainDict

if __name__ == '__main__':
    print calcEntropy([[1,1,'yes'], [1,1,'yes'], [1, 0, 'no'], [1, 0, 'no']])
    print splitFeatureFromSet([[1,2,'yes'],[1,1,'yes'],[0,2,'no']], 0, 1)
    dataSet = [[1,1,'yes'], [1,1,'yes'], [1, 0, 'no'], [1, 1, 'no']]
    print chooseBestFeature(dataSet)