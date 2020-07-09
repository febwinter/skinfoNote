result = []

worldList = list(input('데이터를 입력하세요 : '))

print(worldList)

print('값을 뒤집습니다.')
for i in range(len(worldList)):
    result.append(worldList.pop())
print(result)