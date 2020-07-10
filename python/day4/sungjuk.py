from typing import List # 반환값을 전달하기 위해서 import 함
import os
import report # generate_report()

def runSungjuk()->list:
    for user in sungjuk:
        temp = sungjuk[user]
        if len(temp) < 5: # 리스트의 길이로 총점, 평균을 구했는지 확인한다
            total = temp[0] + temp[1] + temp[2]
            avg = total /3
            temp.extend([total,avg]) # 데이터 병합해서 사용

        #print(user, sungjuk[user])
    
   #  newList = sungjuk.items() # --> ('User1', [100, 90, 80, 270, 90]) 형태의 이중 리스트

    newList = sorted(sungjuk.items(), key=lambda u: u[1][3], reverse=True)
    '''
    lambda 함수 :
    Lambda x : 표현식
    위의 예제에서는 sorted 매서드의 key 파라미터 u에 대해서 Lambda를 써서 넘기는 예제이다.
    u는 sungjuk.items()가 오게 되고 Lambda함수를 통해서 u[1][3]에 해당하는 총점을 키값으로 사용한다.
    '''

    return newList
    
def showSungjuk():
    newList = runSungjuk()
    for user in newList:
        print(user[0], '\t', seperateGrade(user[1]))  


def seperateGrade(data):
    result = ''
    for _num in range(len(data) - 1): # [70, 85, 99, 254] ==> 합까지만 계산
        result += str(data[_num]) + '\t'

    # 평균 계산 (소수 4째자리)
    return result + ('%.4f' % (data[len(data) - 1]))



sungjuk = {}
# sungjuk['USER1'] = [88,70,99]
# sungjuk['USER2'] = [78,100,77]
# sungjuk['USER3'] = [100,90,80]
# sungjuk['USER4'] = [99,80,66]

# 국어, 영어, 수학, 총점, 평균, 석차

# 성적, 출력, 조회, 종료
'''
이름, 총점, 평균만을  표시하는 report.csv 파일을 생성하시오
ex) 
이름, 총점, 평균
USER1,270,90,90
USER2,254,84,67
'''

while True:
    print('## 현재 등록자 수 : {}'.format(len(sungjuk)))
    # 1 ~ 4 입력 허용
    # 입력값을 int()로 casting
    try:
        cmd = int(input('1) 성적 입력\n2) 성적 출력\n3) 성적 조회\n4) 성적 저장\n5) 성적 불러오기\n6) 리포트 출력\n9) 종료\n## 1 ~ 9 에서 선택해 입력하세요 : '))
    except:
        print('** 명령어는 1 ~ 9 사이의 숫자만 입력해 주세요 **')
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

    elif cmd == 4: # 성적 파일 저장
        with open('sungjuk.dat','w',encoding='utf-8')  as file:
            calculatedSungjuk = runSungjuk() # 총점, 평균 안들어간 데이터들 입력 -> 리스트 반환
            for element in calculatedSungjuk: # 각 유저별 데이터가 List의 형태로 element에 들어감
                _name = element[0]              # 0 번째 인덱스에 유저 이름이 들어감 그 뒤로 국,영,수,총점,평균 이 들어감
                file.write(_name+',')
                _nums = element[1] 
                for _number in _nums:
                    file.write('{},'.format(_number))
                file.write('\n')
            print('++ 파일에 저장 하였습니다.')

    elif cmd == 5: # 성적 파일 읽어오기
        tempSungjuk = []
        with open('sungjuk.dat','r',encoding='utf-8') as file:
            for line in file:
                # sungjuk['USER1'] = [100,90,80,총점,평균]
                _values = line.split(',')
                sungjuk[_values[0]] = [int(_values[1]),int(_values[2]),int(_values[3]),int(_values[4]),float(_values[5])]
        print('++ 파일을 읽어왔습니다.')

    elif cmd == 6: # csv 파일 생성
        dir = os.path.dirname(os.path.realpath(__file__))
        inFile = dir + '/sungjuk.dat'
        outFile = dir + '/report.csv'
        report.generate_report(inFile,outFile) # 매서드 호출

    elif cmd == 9: # 종료
        quit()

    else:
        print('exception')