def dutch_flag(inList:list)->list: # 0000 111 222
    tempList = inList
    mid = 1
    i = 0
    j = 0
    k = len(tempList)

    while j < k:
        if tempList[j] < mid:
            tempList[i], tempList[j] = tempList[j], tempList[i]
            i += 1
            j += 1
        elif tempList[j] > mid:
            k -= 1
            tempList[j], tempList[k] = tempList[k], tempList[j]
        else:
            j += 1
    
    return tempList


testList = [2,2,1,2,2,1,2,0,0,1,2]
# while True:
#     try:
#         cnt = int(input('몇회 입력하시겠습니까?'))
#         try:
#             for  in range()
#             int(input('0,1,2 값을 입력하세요'))
#     except:
#         print('유효한 값을 입력해주세요!')

print(dutch_flag(testList))


