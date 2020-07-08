age = int(input('나이를 입력하세요 : '))
hight = int(input('키를 입력하세요 : '))
weight = int(input('몸무게를 입력하세요 : '))

bmi = weight / (hight * hight)
risk = ''

if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
        
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'
        
print('나이 {}, BMI {}일 경우 RISK는 {} 입니다.'.format(age,bmi,risk))