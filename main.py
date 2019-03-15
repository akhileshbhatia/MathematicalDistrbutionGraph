'''
Created on Mar 15, 2019

@author: akhilesh
'''
# filename progression seed numOfIterations par1(optional)
import sys
import random
import math

    
def generateSequence(seed,distribution,totalIterations):
    sequence = []
    random.seed(seed)
    if distribution == "Geometric":
        denominator = math.log(1-0.01) #p = 0.01 so denominator is constant
        for i in range(totalIterations):
            sequence.append(math.ceil(math.log(random.uniform(0.0,1.0))/denominator))
    return sequence

def getDictWithCount(sequence):
    dict = {}
    for i in range(len(sequence)):
        key = sequence[i]
        if key in dict: #update current count by 1 if key exists in dictionary
            dict[key] = dict[key] + 1 
        else:
            dict[key] = 1
    
#     print("sequence length ",len(sequence))
#     for key,val in dict.items():
#         print(key,"=>",val)
    return dict
    
    
def geometric():
    sequence = generateSequence(int(sys.argv[2]),"Geometric", int(sys.argv[3]))
    dict = getDictWithCount(sequence)
    for key,value in dict.items():
        dict[key] = value/len(sequence) #calculate probablity
    total = 0.0
    for key,value in dict.items():
#         print(key,"=>",value)
        total = total + value  
    print(total)  
        
        

if sys.argv[1].lower() == "geometric":
    geometric()
else:
    print("Something wrong with the parameters. Please try again")
    

    
