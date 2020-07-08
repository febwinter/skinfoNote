# kor, eng, mat 세과목의 총점과 평균을 구하는 함수를 생성
# 총점 함수 : sum
# 평균 함수 : avg

def sum(kor, eng, mat):
    return kor + eng + mat

def avg(kor, eng, mat):
    return round(sum(kor, eng, mat) / 3, 2)


name = input("이름을 입력하세요 : ")
kor = float(input("국어 점수를 입력하세요 : "))
eng = float(input("영어 점수를 입력하세요 : "))
mat = float(input("수학 점수를 입력하세요 : "))

print('Name : ' + name)
#print(name + '의 Sumation : ', sum(kor,eng,mat))
#print(name + '의 Average : ', avg(kor,eng,mat))

print('{}의 Sumation : {}'.format(name, sum(kor,eng,mat)))
print('{}의 Average : {}'.format(name, avg(kor,eng,mat)))

# 1. 사용자 이름 입력
# 2. 평균을 소수점 2자리에서 반올림