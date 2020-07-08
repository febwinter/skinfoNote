# 가위 바위 보 게임
# 1. 사용자로부터 가위, 바위, 보를 입력
# 2. 컴퓨터가 임의의 가위, 바위, 보를 생성
# 3. 사용자와 컴퓨터간의 가위, 바위, 보 판정
# 4. 사용자와 컴퓨터 중 누가 이겼는지 출력
# 5. 게임 종료 시 게임을 중단할 지, 계속 할지 물어봄

import random

comAns = random.randrange(3)
restart = True



while(restart):
    comAns = random.randrange(3)
    while True:
        usrAns = int(input('가위, 바위, 보를 선택하세요 : (가위 : 1, 바위 : 2, 보 : 3) : '))
        if usrAns != 1 and usrAns != 2 and usrAns != 3:
            print('1, 2, 3 중에 선택해주세요')
        else:
            break

    if(comAns == 1): # 가위
        print('컴퓨터 : 가위!')
        if(usrAns == 1):
            # 무승부
            print('유저 : 가위!')
            print("비겼습니다")
        elif(usrAns == 2):
            # 승리
            print('유저 : 바위!')
            print('이겼습니다')
            restart = False
        else:
            # 패배
            print('유저 : 보!')
            print('졌습니다.')
            restart = False
    elif(comAns == 2): # 바위
        print('컴퓨터 : 바위!')
        if(usrAns == 1):
            # 패배
            print('유저 : 가위!')
            print('졌습니다.')
            restart = False
        elif(usrAns == 2):
            # 무승부
            print('유저 : 바위!')        
            print("비겼습니다")
        else:
            # 승리
            print('유저 : 보!')
            print('이겼습니다')
            restart = False
    elif(comAns == 3): # 보
        print('컴퓨터 : 보!')
        if(usrAns == 1):
            # 승리
            print('유저 : 가위!')
            print('이겼습니다')
            restart = False
        elif(usrAns == 2):
            # 패배
            print('유저 : 바위!')
            print('졌습니다.')
            restart = False
        else:
            # 무승부
            print('유저 : 보!')
            print("비겼습니다")
    print('\n\n')
    if restart == False:
        while True:
            answer = int(input('계속 하시겠습니까? : (yes : 1, no : 2) : '))
            if answer != 1 and answer != 2:
                print('1, 2, 3 중에 선택해주세요')
        if answer == 1:
            restart = True

print('='*30)
print('게임이 종료되었습니다!')
