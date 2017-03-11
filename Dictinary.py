MyDict = {'jan':1, 'feb':2, 'mar':3, 1:'jan', 2:'feb', 3:'mar'}
print MyDict['jan']
print MyDict[1]
MyDict['apr']=4

collect=[]
for value in MyDict:
    collect.append(value)
print collect
print MyDict
print MyDict.keys() # Return the value in MyDict.