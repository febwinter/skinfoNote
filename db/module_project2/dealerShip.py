'''
- 고객 - CRUD (추가, 조회, 갱신, 삭제)
- 자동차 - CRUD (추가, 조회, 갱신, 삭제)
- 구매 - 고객 ID, 자동차 목록, 구매 
        * 고객 ID 요구
        * 차량 목록 표시 (car table에서 테이블 가져오기)
        * 구매 차량 정보 표시 (해당 row에 대한 정보만 표시)
        * 인보이스 파일로 내보내기

- 서비스 - 날짜 가능여부, 신청, 조회
        * 고객 ID, 차량 시리얼 넘버 요구
        * 서비스 날짜 조회
        * 사용 가능 정비공 선택 (없을 경우 날짜 선택할수 없음 메세지)
        * (고객 ID, 차량 시리얼넘버, 예약 날짜, 정비공) 으로 신청

        * 신청 목록 조회 (사용자 ID or 차량 시리얼넘버로 검색 가능하게)
'''
# 필요 파이썬 모듈
'''
docker 이미지 생성시 필요 설치 사항

pip3 install pymysql
pip3 install prettytable 
'''
import os
import pymysql
from prettytable import PrettyTable 
import customerMenu
import carMenu


##################################################################################################

# 메인 메뉴
'''
메인 메뉴 설정
'''
def Main_Menu(curs)-> bool:
    
    # 제목 출력
    print('+'*50)
    print('{:^50s}'.format("Car Dealership"))
    print('+'*50)

    # 메뉴 출력
    print('<<메뉴를 선택하세요>>')
    print("""
1. 고객 관리

2. 차량 관리

3. 차량 구매

4. 차량 서비스

5. 종료""")

    while True:
        try:
            sel = int(input('메뉴 번호를 선택해주세요 : '))
            if sel != 1 and sel != 2 and sel != 3 and sel !=4 and sel != 5:
                raise Exception
            else:
                break

        except:
            print('유효한 값을 입력해주세요')
            
    if sel == 1:
        CRUD_Customer(curs)
        return True
    elif sel == 2:
        CRUD_Car(curs)
        return True
    elif sel == 3:
        Purchase_Car(curs)
        return True
    elif sel == 4:
        Service_Car(curs)
        return True
    elif sel == 5:
        return False

#################################################################################################

# 1. 고객 관리
# 1-1. 고객 등록 - 목록에 고객 인적사항 추가
# 1-2. 고객 조회 - 고객 목록을 테이블에서 가져와 출력
# 1-3. 고객 갱신 - 특정 고객 인적사항 수정
# 1-4. 고객 삭제 - 목록에서 특정 고객 인적사항 삭제

def CRUD_Customer(curs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('고객 관련 메뉴입니다')
    print("""

1. 고객 등록

2. 고객 정보 조회

3. 고객 정보 갱신

4. 고객 정보 삭제

5. 뒤로가기""")
    while True:
        try:
            sel = int(input('메뉴 번호를 선택해주세요 : '))
            if sel != 1 and sel != 2 and sel != 3 and sel !=4 and sel != 5:
                raise Exception
            else:
                break

        except:
            print('유효한 값을 입력해주세요')
            
    if sel == 1:
        # 고객 등록
        return True
    elif sel == 2:
        # 고객 정보 조회
        return True
    elif sel == 3:
        # 고객 정보 갱신
        return True
    elif sel == 4:
        # 고객 정보 삭제
        return True
    elif sel == 5:
        # 뒤로가기
        return False

    return 0

##################################################################################################

# 2. 차량 관리
def CRUD_Car(curs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('차량 관련 메뉴입니다')
    print("""

1. 차량 등록

2. 차량 정보 조회

3. 차량 정보 갱신

4. 차량 정보 삭제

5. 뒤로가기""")

    while True:
        try:
            sel = int(input('메뉴 번호를 선택해주세요 : '))
            if sel != 1 and sel != 2 and sel != 3 and sel !=4 and sel != 5:
                raise Exception
            else:
                break

        except:
            print('유효한 값을 입력해주세요')
            
    if sel == 1:
        # 차량 등록
        return True
    elif sel == 2:
        # 차량 정보 조회
        return True
    elif sel == 3:
        # 차량 정보 갱신
        return True
    elif sel == 4:
        # 차량 정보 삭제
        return True
    elif sel == 5:
        # 뒤로가기
        return False
    
    return 0

###################################################################################################

# 3. 차량 구매
def Purchase_Car(curs):
    print('차량 구매 메뉴입니다')
    return 0

###################################################################################################

# 4. 차량 서비스
def Service_Car(curs):
    print('차량 수비 서비스 입니다')
    return 0

###################################################################################################

# Database Connect Function
def DB_Connection(host:str, port:int, user:str, password:str, db:str, charset:str):
    return pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset)

###################################################################################################

# Query Print Function
def Show_DB(curs,query:str):
    col = []
    curs.execute(query)
    
    for col_object in curs.description:
        col.append(col_object[0])
    
    t = PrettyTable(col)
    
    for row in curs.fetchall():
        t.add_row(row)
    
    print(t)

###################################################################################################

# 데이터베이스 연결
con = DB_Connection('localhost',3306,'root','password','repl_db','utf8')
#데이터 변수 조작 커서 할당
curs = con.cursor()

# 메인 메뉴 호출
'''
종료시까지 반복 실행
'''
loop_checker = True
while loop_checker:
    loop_checker = Main_Menu(curs)
    print('\n\n\n\n')
