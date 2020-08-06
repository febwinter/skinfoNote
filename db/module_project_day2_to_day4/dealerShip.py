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

(추가)
- 정비공 CRUD
- 부품 CRUD
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
# import customerMenu
# import carMenu


##################################################################################################

# 메인 메뉴
'''
메인 메뉴 설정
'''
def Main_Menu(conn,curs)-> bool:
    
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
        CRUD_Customer(conn, curs)
        return True
    elif sel == 2:
        CRUD_Car(conn, curs)
        return True
    elif sel == 3:
        Purchase_Car(conn, curs)
        return True
    elif sel == 4:
        Service_Car(conn, curs)
        return True
    elif sel == 5:
        return False

#################################################################################################

# 1. 고객 관리
# 1-1. 고객 등록 - 목록에 고객 인적사항 추가
# 1-2. 고객 조회 - 고객 목록을 테이블에서 가져와 출력
# 1-3. 고객 갱신 - 특정 고객 인적사항 수정
# 1-4. 고객 삭제 - 목록에서 특정 고객 인적사항 삭제

def CRUD_Customer(conn, curs):
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
        CustReg(conn, curs)
        return True
    elif sel == 2:
        # 고객 정보 조회
        CustSearch(conn,curs)
        return True
    elif sel == 3:
        # 고객 정보 갱신
        CustUpdate(conn,curs)
        return True
    elif sel == 4:
        # 고객 정보 삭제
        CustDrop(conn,curs)
        return True
    elif sel == 5:
        # 뒤로가기
        return False

    return 0

##################################################################################################

# 1-1 고객 등록
# insert into Customer (name, phone, address, e_mail) values('Arron', '010-0000-0000', 'seoul', 'arron@abc.com');
def CustReg(conn, curs):
    print('고객 등록 관련 메뉴입니다\n')
    while True:
        print('등록할 고객 정보를 입력해주세요\n')

        try:
            name = input('이름 : ')
            phone = input("전화번호('-'를 포함) : ")
            address = input('주소 : ')
            mail = input('email : ')
            insertSql = "insert into Customer(name, phone, address, e_mail) values('{}','{}','{}','{}');".format(name, phone, address, mail)
            curs.execute(insertSql)
            conn.commit()
            print('\n등록되었습니다!\n')
            Show_DB(curs,"select * from Customer where name like '{}' and phone like '{}';".format(name,phone))
            break
        except:
            print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')

##################################################################################################

# 1-2 고객 정보 조회

def CustSearch(conn, curs):
    print('고객 검색 관련 메뉴입니다\n')
    loop_checker = True
    while loop_checker:
        loop_checker = SearchTable(conn, curs, "select * from Customer c where c.customer_id like '%{0}%' or c.name like '%{0}%' or c.phone like '%{0}%' or c.e_mail like '%{0}%';",'need type')

##################################################################################################
# 1-3 고객 정보 갱신

def CustUpdate(conn, curs):
    print('\n고객 정보 갱신 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Customer c where c.customer_id like '%{0}%' or c.name like '%{0}%' or c.phone like '%{0}%' or c.e_mail like '%{0}%';",'need type')
            if loop_checker == False:
                raise Exception
        except Exception as ex:
            # 미리 나갈수 있는 분기
            break

        # 검색 결과가 여러개인 경우 --> 결과 내 재검색
        if len(resultList) > 1:
            print('-'*50)
            print('{:^50s}'.format("\n<<결과 내 재검색>> 검색 내용에 중복되는 검색 결과가 존재합니다\n"))
            print('-'*50)
            while True:
                try:
                    idNum = int(input('\n ** 검색 결과 중 해당하는 고객 id (customer_id)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Customer c where c.customer_id like {}".format(idNum))
                    break
                
                except:
                    print('\n<<유효한 값을 입력해 주세요>>\n')
        
        # 검색 데이터가 없는 경우
        elif len(resultList) < 1:
            print('\n<<검색 데이터가 없습니다>>\n')
            errChecker = True

        # 검색 결과가 하나인 경우
        else:
            idNum = resultList[0][0]
        
        # 고객정보 갱신 부분 (name, phone, address, e_mail)
        if idNum != -1 and errChecker == False:
            print("\n<<해당 고객에 대한 고객 정보 갱신을 시작합니다>>\n")
            while True:
                try:
                    u_name = input('name : ')
                    u_phone = input('phone : ')
                    u_address = input('address : ')
                    u_e_mail = input('e-mail : ')
                    break
                except:
                    print("\n<<유효한 값을 입력하세요>>\n")
            try:
                curs.execute("update Customer set name='{}',phone='{}',address='{}',e_mail='{}' where customer_id={}".format(u_name,u_phone,u_address,u_e_mail,idNum))
                conn.commit()

                Show_DB(curs,"select * from Customer c where c.customer_id={}".format(idNum))
                print('\n<<업데이트 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<업데이트에 실패했습니다>>\n')
                print(ex)
            
        else:
            print('\n\n<<업데이트를 취소했습니다>>\n\n')


##################################################################################################
# 1-4 고객정보 삭제

def CustDrop(conn,curs):
    print('\n고객 정보 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Customer c where c.customer_id like '%{0}%' or c.name like '%{0}%' or c.phone like '%{0}%' or c.e_mail like '%{0}%';",'need type')
            if loop_checker == False:
                raise Exception
        except Exception as ex:
            # 미리 나갈수 있는 분기
            print(ex)
            break

        # 검색 결과가 여러개인 경우 --> 결과 내 재검색
        if len(resultList) > 1:
            print('-'*50)
            print('{:^50s}'.format("\n<<결과 내 재검색>> 검색 내용에 중복되는 검색 결과가 존재합니다\n"))
            print('-'*50)
            while True:
                try:
                    idNum = int(input('\n ** 검색 결과 중 해당하는 고객 id (customer_id)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Customer c where c.customer_id like {}".format(idNum))
                    break
                
                except:
                    print('\n<<유효한 값을 입력해 주세요>>\n')
        
        # 검색 데이터가 없는 경우
        elif len(resultList) < 1:
            print('\n<<검색 데이터가 없습니다>>\n')
            errChecker = True

        # 검색 결과가 하나인 경우
        else:
            idNum = resultList[0][0]
        
        # 고객정보 삭제 부분
        if idNum != -1 and errChecker == False:
            print("\n<<해당 고객에 대한 고객 정보 삭제을 시작합니다>>\n")
            
            try:
                curs.execute("delete from Customer where customer_id={};".format(idNum))
                conn.commit()
                print('\n<< 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<삭제 실패!>>\n')
                print(ex)
            
        else:
            print('\n\n<<정보 삭제를 취소했습니다>>\n\n')



##################################################################################################

# 2. 차량 관리
# 2-1. 차량 등록 - 목록에 고객 인적사항 추가
# 2-2. 차량 정보 조회 - 고객 목록을 테이블에서 가져와 출력
# 2-3. 차량 정보 갱신 - 특정 고객 인적사항 수정
# 2-4. 차량 정보 삭제 - 목록에서 특정 고객 인적사항 삭제

def CRUD_Car(conn, curs):
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
        CarReg(conn,curs)
        return True
    elif sel == 2:
        # 차량 정보 조회
        CarSearch(conn,curs)
        return True
    elif sel == 3:
        # 차량 정보 갱신
        CarUpdate(conn,curs)
        return True
    elif sel == 4:
        # 차량 정보 삭제
        CarDrop(conn,curs)
        return True
    elif sel == 5:
        # 뒤로가기
        return False
    
    return 0

###################################################################################################
# 2-1 차량 등록
def CarReg(conn,curs):
    print('차량 등록 관련 메뉴입니다\n')
    while True:
        print('등록할 차량 정보를 입력해주세요\n')

        try:
            c_seller_id = int(input('판매자 ID : '))
            c_car_model = input("차량 모델 : ")
            c_price = int(input('가격 : '))
            while True:
                try:
                    temp_used = input('중고 여부 (신차/중고차) : ')
                    
                    if temp_used == '신차':
                        c_used = False
                    elif temp_used == '중고차':
                        c_used = True
                    else:
                        raise Exception

                except:
                    print('\n<<신차/중고차 중 하나를 입력해 주세요>>\n')

            insertSql = "insert into car_list(seller_id, car_model, used, price) values({},'{}', {}, {} );".format(c_seller_id, c_car_model, c_used, c_price)
            curs.execute(insertSql)
            conn.commit()
            print('\n등록되었습니다!\n')
            Show_DB(curs,"select * from car_list where seller_id={} and car_model like '{}' and used={} and price={};".format(c_seller_id, c_car_model, c_used, c_price)
            break
        except:
            print('\n유효한 값을 입력해주세요\n')
    
###################################################################################################
# 2-2 차량 정보 조회
def CarSearch(conn,curs):
    print('차량 검색 관련 메뉴입니다\n')
    while True:
        try:
            print("")

        except:

    

    loop_checker = True
    while loop_checker:
        loop_checker = SearchTable(conn, curs, "select cl.serial_no, cl.car_model, cl.price, s.name, s.phone, s.store from car_list cl, Seller s where cl.seller_id =s.seller_id where cl.serial_no='%{0}%' or cl.car_model='%{0}%' or cl.price='%{0}%' or s.name='' or s.phone='' or s.store='' order by s.name;",'need type')
        
###################################################################################################
# 2-3 차량 정보 갱신
def CarUpdate(conn,curs):
    return 0
###################################################################################################
# 2-4 차량 정보 삭제
def CarDrop(conn,curs):
    return 0


###################################################################################################

# 3. 차량 구매
def Purchase_Car(conn, curs):
    print('차량 구매 메뉴입니다')
    return 0

###################################################################################################

# 4. 차량 서비스
def Service_Car(conn, curs):
    print('차량 수비 서비스 입니다')
    return 0

###################################################################################################

# Database Connect Function
def DB_Connection(host:str, port:int, user:str, password:str, db:str, charset:str):
    con = pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
    return con, con.cursor()

###################################################################################################

# Query Print Function
def Show_DB(curs,query:str):
    col = []
    curs.execute(query)
    
    for col_object in curs.description:
        col.append(col_object[0])
    
    t = PrettyTable(col)
    resultList = []
    
    for row in curs.fetchall():
        t.add_row(row)
        resultList.append(row)
    
    print(t)
    return resultList

##################################################################################################
# Search Function

def SearchTable(conn, curs, searchSql:str, keyword):
    try:
        print('검색어를 입력하세요\n\n')
        keyword = input("검색어 (종료를 원할시 '끝내기'를 입력해주세요) : ")
        if keyword == '끝내기':
            return False, []
        else:
            print('-'*50)
            print('{:^50s}'.format("검색 결과"))
            print('-'*50)
            resultList = Show_DB(curs,searchSql.format(keyword))
            print('검색 결과 갯수 : {}\n'.format(len(resultList)))
            return True, resultList
    except Exception as ex:
        print('{:^50s}'.format('\n<<<오류가 발생했습니다. 적절한 검색 값을 입력해주세요>>>\n'))
        print(ex)
        return True

###################################################################################################

# 데이터베이스 연결 및 커서 할당
con, curs = DB_Connection('localhost',3306,'root','password','Car_Dealership','utf8')
#데이터 변수 조작 커서 할당
# curs = con.cursor()

# 메인 메뉴 호출
'''
종료시까지 반복 실행
'''
loop_checker = True
while loop_checker:
    loop_checker = Main_Menu(con,curs)
    print('\n\n\n\n')
con.close()