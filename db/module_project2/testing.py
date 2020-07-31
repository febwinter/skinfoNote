# def formatstringTest(testStr,testarg):
#     testarg = input('입력 : ')
#     print(testStr.format(testarg))

# formatstringTest("This is {0} test file for {0} test",'none')

# print(list(range(1,14 + 1)))

# t_list = [(1,2,3,4),(2,3,4,5),(6,7,8,9),(10,11,12,13)]

# print([t_list[i][0] for i in range(4)])

from datetime import datetime

now = datetime.now()
pur_date = now.strftime('%Y-%m-%d')

print(pur_date)