# def showSungjuk(df):
#     for name, score in df.items():
#         sum = sum(score)
#         avg = round(sum / 3,4)
#         print('{}\t{}\t{}\t{}\t{}\t{}'.format(name,score[0],score[1],score[2],sum,avg))
#     return None

def showSungjuk():
    for user in sungjuk:
        temp = sungjuk[user]
        if len(temp) < 5: # 리스트의 길이로 총점, 평균을 구했는지 확인한다
            total = temp[0] + temp[1] + temp[2]
            avg = total /3
            temp.extend([total,avg]) # 데이터 병합해서 사용

        #print(user, sungjuk[user])
    
   #  newList = sungjuk.items() # --> ('User1', [100, 90, 80, 270, 90]) 형태의 이중 리스트

    newList = sorted(sungjuk.items(), key=lambda u: u[1][3], reverse=True)

    for user in newList:
        print(user[0], '\t', seperateGrade(user[1]))


def seperateGrade(data):
    result = ''
    for _num in range(len(data) - 1): # [70, 85, 99, 254] ==> 합까지만 계산
        result += str(data[_num]) + '\t'

    # 평균 계산 (소수 4째자리)
    return result + ('%.4f' % (data[len(data) - 1]))



sungjuk = {}
sungjuk['USER1'] = [88,70,99]
sungjuk['USER2'] = [78,100,77]
sungjuk['USER3'] = [100,90,80]
sungjuk['USER4'] = [99,80,66]

# 국어, 영어, 수학, 총점, 평균, 석차

# 성적, 출력, 조회, 종료

while True:
    print('## 현재 등록자 수 : {}'.format(len(sungjuk)))
    # 1 ~ 4 입력 허용
    # 입력값을 int()로 casting
    try:
        cmd = int(input('1) 성적 입력\n2) 성적 출력\n3) 성적 조회\n4) 종료\n## 1 ~ 4 에서 선택해 입력하세요 : '))
    except:
        print('** 명령어는 1 ~ 4 사이의 숫자만 입력해 주세요 **')
        continue

    if cmd == 1: # 성적 입력
        '''
        입력조건 1) 이름, 국어, 영어, 수학
        입력조건 2) 각 과목의 점수는 0 ~ 100점 사이
        '''
        while True:
            try:
                newName = input('이름을 입력하세요 : ')
                temp = input('성적을 입력하세요(점수는 ","로 구분해주세요) : ').split(',')
                newScore = list(map(int,temp))
                
                if len(newScore) != 3:
                    raise Exception
            
                else: # OK
                    kor = newScore[0]
                    eng = newScore[1]
                    mat = newScore[2]

                    if kor < 0 or kor > 100:
                        raise Exception
                    if eng < 0 or eng > 100:
                        raise Exception
                    if mat < 0 or eng > 100:
                        raise Exception
                    
            except Exception as ex:
                print('성적을 정확하게 입력해주세요')
                continue

            else:
                sungjuk[newName] = newScore # sungjuk['USER] = [x , y , z]
                print('성적 입력 완료!')
                print()
                break


    elif cmd == 2: # 성적 출력
        print('#' * 50)
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('#' * 50)
        showSungjuk()
        print()

    elif cmd == 3: # 성적 조회
        try:
            searchUser = input('검색할 사용자명을 입력하세요 : ')
            exsist = list(sungjuk.keys()).index(searchUser)

            if(exsist < 0):
                raise Exception
        
        except Exception as ex:
            print('해당 사용자는 존재하지 않는 사용자입니다')

        else:
            sUser = sungjuk[searchUser]
            print('#' * 50)
            print('이름\t국어\t영어\t수학\t총점\t평균')
            print('#' * 50)
            print(sUser[0], '\t', seperateGrade(sUser[1]))
            print(sungjuk[searchUser])
            print()

    elif cmd == 4: # 종료
        quit()

    else:
        print('exception')