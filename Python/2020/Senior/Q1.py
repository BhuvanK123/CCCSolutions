import math

N = int(input()) # Number of Observations

dic = {}
dic2 = {}

for num in range(N):
    obv = input().split() #Observation
    dic.update({int(obv[0]) : int(obv[1])})

for i in sorted(dic):
   dic2[i]=dic[i]

indexedKeys = list(dic2)
indexedValues = list(dic2.values())

newAns = 0

for items in range(len(indexedKeys)-1):
    subKeys = indexedKeys[items+1] - indexedKeys[items]
    subValues = indexedValues[items+1] - indexedValues[items]

    Ans = abs(subValues/subKeys)

    if newAns < Ans:
        newAns = Ans

print(newAns)
