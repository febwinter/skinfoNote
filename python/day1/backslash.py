#print('\\10,000')
#print('Albert\t Einstein')
#print('Albert\t\tEinstein\n\\10,000')

# numbers = '''one
# \ttwo
# \t\tthree'''

# print(numbers)
# print()

# 세명의 학생에 대해 국어, 영어, 수학 성적을 읿력받은 다음 총점이 가장 높은 점수가 몇점인지 출력하시오.
maxScore = 0
sum = 0
for i in range(3):
    sum += float(input("학생{}의 국어성적을 입력하세요 : ".format(i+1)))
    sum += float(input("학생{}의 영어성적을 입력하세요 : ".format(i+1)))
    sum += float(input("학생{}의 수학성적을 입력하세요 : ".format(i+1)))

    if(sum >= maxScore):
        maxScore = sum
        sum = 0
    else:
        sum = 0

print(maxScore)