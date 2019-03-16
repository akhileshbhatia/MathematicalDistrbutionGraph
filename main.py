'''
Created on Mar 15, 2019

@author: akhilesh
'''

import sys
import random
import math
import collections
import matplotlib.pyplot as plt
    
def generateDistributionSequence(seed,distribution,totalIterations,par1=None,par2=None):
    sequence = []
    random.seed(seed)
    if distribution == "Geometric":
        denominator = math.log(1-0.01) #p = 0.01 so denominator is constant
        for i in range(totalIterations):
            sequence.append(round((math.log(random.uniform(0.0,1.0))/denominator),2))
#             
    if distribution == "Exponential":
        lambdaVal = par1
        for i in range(totalIterations):
            sequence.append(round((-math.log(1-random.uniform(0.0,1.0))/lambdaVal),2))
    
    if distribution == "Power":
        alpha = par1
        beta = par2
        for i in range(totalIterations):
            sequence.append(round(alpha * math.pow(random.uniform(0.0,1.0),1/beta),2))
    return sequence

def getDictWithProbablity(sequence):
    dict = collections.OrderedDict()
    sequenceLength = len(sequence)
    #calculate Count
    for i in range(sequenceLength):
        key = sequence[i]
        if key in dict: #update current count by 1 if key exists in dictionary
            dict[key] = dict[key] + 1 
        else:
            dict[key] = 1
    
    #calculate probability
    for key,value in dict.items():
        dict[key] = value/sequenceLength 
    return dict
    
def getCumSum(sequence):
    sequenceLength = len(sequence)
    cumSum = [None]*sequenceLength
    cumSum[0] = sequence[0]
    for i in range(1,sequenceLength):
            cumSum[i] = round(cumSum[i-1] + sequence[i],2)
    return cumSum

def writeToFile(obj1,obj2=None):
    if(obj2 == None):
        print("Writing sequence to file...")
        with open("sequence.txt", "w") as f:
            for item in obj1:
                f.write(str(item) + "\n")
    else:
        print("Writing cdf data to file...")
        with open("cdf.txt","w") as f:
            for i in range(len(obj1)):
                f.write(str(obj1[i]) + " " + str(obj2[i]) + "\n")

def generateCompleteDistributionData():
# filename distributionType seed numOfIterations par1(optional) par2(optional)
    print("Generating sequence...")
    if sys.argv[1].lower() == "geometric":
        sequence = generateDistributionSequence(int(sys.argv[2]),"Geometric", int(sys.argv[3]))
    if sys.argv[1].lower() == "exponential":
        sequence = generateDistributionSequence(int(sys.argv[2]),"Exponential", int(sys.argv[3]), float(sys.argv[4]))
    if sys.argv[1].lower() == "power":
        sequence = generateDistributionSequence(int(sys.argv[2]),"Power", int(sys.argv[3]), float(sys.argv[4]),float(sys.argv[5]))
    sequence.sort()
    writeToFile(sequence)
    
    print("Generating cdf data...")
    dictProb = getDictWithProbablity(sequence)
    cumSum = getCumSum(list(dictProb.values()))
    writeToFile(list(dictProb.keys()),cumSum)
    
    return dictProb.keys(), cumSum


f = plt.figure()
xData, yData = generateCompleteDistributionData()
print("Generating plot...")
if sys.argv[1].lower() == "geometric":
    plt.step(xData,yData)
else:
    plt.plot(xData,yData)
# plt.show()
print("Saving plot to file...")

f.savefig("plot.pdf",bbox_inches="tight")
print("All files generated. Please check the current folder.")


    

    
