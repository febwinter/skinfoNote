import random
count = 0
comNum = random.randrange(1,100)
#print(comNum)

while True:
    usrNum = int(input('숫자를 입력하세요(1-100): '))
    count += 1
    if usrNum < 1 or usrNum > 100:
        print('1-100 사이의 숫자만 입력해주세요')
    else:
        if comNum > usrNum:
            print('더 큰 숫자를 입력하세요')
        
        elif comNum < usrNum:
            print('더 작은 숫자를 입력하세요')
        
        else: # comNum == usrNum
            print('맞췄습니다')
            print('=' * 30)
            print('COMPUTER NUMBER : {}'.format(comNum))
            if count > 7:
                print('{}번만에 맞췄습니다. 당신은 바보입니다.'.format(count))
            elif count > 3:
                print('{}번만에 맞췄습니다. 당신은 보통입니다.'.format(count))
            else:
                print('{}번만에 맞췄습니다. 당신은 천재입니다.'.format(count))
            break # 근접한 루프 실행을 종료