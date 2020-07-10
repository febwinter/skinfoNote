import time

def findMinOrMax(inputList:list, order:bool)->tuple:
    minimum = inputList[0]
    maximum = inputList[0]
    if order:
        for element in inputList:
            if element < minimum:
                minimum = element
        minIndex = inputList.index(minimum)
        ans = (minimum, minIndex)
        return ans
    else:
        for element in inputList:
            if element > maximum:
                maximum = element
        maxIndex = inputList.index(maximum)
        ans = (maximum, maxIndex)
        return ans    

def minMax(inList:list, order:bool)->tuple:
    if order:
        return (min(inList), inList.index(min(inList)))
    else:
        return (max(inList), inList.index(max(inList)))

testCase = [1,2,3,4,5,6,7,8,9,12,33]
t1 = time.perf_counter()
print(findMinOrMax(testCase,True))
print(findMinOrMax(testCase,False))
t2 = time.perf_counter()
print('Time : {}'.format(t2 - t1))

t1 = time.perf_counter()
print(minMax(testCase,True))
print(minMax(testCase,False))
t2 = time.perf_counter()
print('Time : {}'.format(t2 - t1))  