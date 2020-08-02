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
from datetime import datetime
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

5. 구매 내역 삭제

6. 부품 관리

7. 메카닉 관리

8. 종료

""")

    while True:
        try:
            sel = int(input('메뉴 번호를 선택해주세요 : '))
            if sel != 1 and sel != 2 and sel != 3 and sel !=4 and sel != 5 and sel != 6 and sel != 7 and sel != 8:
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
        Make_Invoice(conn, curs)
        return True
    elif sel == 4:
        Service_Car(conn, curs)
        return True
    elif sel == 5:
        # 구매 내역 삭제
        Drop_Invoice(conn, curs)
        return True
    elif sel == 6:
        CRUD_Parts(conn, curs)
        return True
    elif sel == 7:
        CRUD_Mechanic(conn, curs)
        return True 
    elif sel == 8:
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
        loop_checker, ls = SearchTable(conn, curs, "select * from Customer c where c.customer_id like '%{0}%' or c.name like '%{0}%' or c.phone like '%{0}%' or c.e_mail like '%{0}%';",'need type')

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
            print("\n<<해당 고객에 대한 정보 삭제를 시작합니다>>\n")
            
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
            c_model = input("차량 모델 : ")
            while True:
                try:
                    temp = input('중고 여부 (신차/중고) : ')
                    if temp == '신차':
                        c_used = 'False'
                    elif temp == '중고':
                        c_used = 'True'
                    else:
                        raise Exception
                    break
                except:
                    print('\n<<정해진 값 중 선택해 입력해 주세요>>\n')
            c_price = int(input('가격 : '))
            insertSql = "insert into car_list(seller_id, car_model, used, price) values({},'{}', {}, {} );".format(c_seller_id, c_model, c_used, c_price)
            curs.execute(insertSql)
            conn.commit()
            print('\n등록되었습니다!\n')
            Show_DB(curs,"select * from car_list where seller_id={} and car_model like '{}' and used={} and price={};".format(c_seller_id, c_model, c_used, c_price))
            break
        except Exception as ex:
            print('\n유효한 값을 입력해주세요\n')
            print(ex)
###################################################################################################
# 2-2 차량 정보 조회
def CarSearch(conn,curs):
    print('차량 검색 관련 메뉴입니다\n')
    loop_checker = True
    while loop_checker:
        loop_checker, ls = SearchTable(conn, curs, "select cl.serial_no, cl.car_model, cl.price, s.name, s.phone, s.store from car_list cl, Seller s where cl.seller_id =s.seller_id and (convert(cl.serial_no, char) like '%{0}%' or cl.car_model like '%{0}%' or convert(cl.price, char) like '%{0}%' or s.name like '%{0}%' or s.phone like '%{0}%' or s.store like '%{0}%') group by cl.serial_no;",'need type')

###################################################################################################
# 2-3 차량 정보 갱신
def CarUpdate(conn,curs):
    print('\n차량 정보 갱신 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select cl.serial_no, cl.car_model, cl.price, s.name, s.phone, s.store from car_list cl, Seller s where cl.seller_id =s.seller_id and (convert(cl.serial_no, char) like '%{0}%' or cl.car_model like '%{0}%' or convert(cl.price, char) like '%{0}%' or s.name like '%{0}%' or s.phone like '%{0}%' or s.store like '%{0}%') group by cl.serial_no;",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 차량 시리얼 번호(serial_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from car_list c where c.serial_no like {}".format(idNum))
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
        
        # 차량 정보 갱신 부분 (name, phone, address, e_mail)
        if idNum != -1 and errChecker == False:
            print("\n<<해당 차량에 대한 고객 정보 갱신을 시작합니다>>\n")
            while True:
                try:
                    c_seller_id = int(input('판매자 ID : '))
                    c_model = input("차량 모델 : ")
                    while True:
                        try:
                            temp = input('중고 여부 (신차/중고) : ')
                            if temp == '신차':
                                c_used = 'False'
                            elif temp == '중고':
                                c_used = 'True'
                            else:
                                raise Exception
                            break
                        except:
                            print('\n<<정해진 값 중 선택해 입력해 주세요>>\n')
                    c_price = int(input('가격 : '))
                    break
                except:
                    print("\n<<유효한 값을 입력하세요>>\n")
            try:
                curs.execute("update car_list set seller_id={},car_model='{}',used={},price={} where serial_no={}".format(c_seller_id,c_model,c_used,c_price,idNum))
                conn.commit()

                Show_DB(curs,"select * from car_list c where c.serial_no={}".format(idNum))
                print('\n<<업데이트 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<업데이트에 실패했습니다>>\n')
                print(ex)
            
        else:
            print('\n\n<<업데이트를 취소했습니다>>\n\n')


###################################################################################################
# 2-4 차량 정보 삭제
def CarDrop(conn,curs):
    print('\n차량 정보 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select cl.serial_no, cl.car_model, cl.price, s.name, s.phone, s.store from car_list cl, Seller s where cl.seller_id =s.seller_id and (convert(cl.serial_no, char) like '%{0}%' or cl.car_model like '%{0}%' or convert(cl.price, char) like '%{0}%' or s.name like '%{0}%' or s.phone like '%{0}%' or s.store like '%{0}%') group by cl.serial_no;",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 차량 시리얼 번호(serial_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from car_list c where c.serial_no like {}".format(idNum))
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
        
        # 차량 정보 삭제 부분
        if idNum != -1 and errChecker == False:
            print("\n<<해당 차량에 대한 정보 삭제를 시작합니다>>\n")
            
            try:
                curs.execute("delete from car_list where serial_no={};".format(idNum))
                conn.commit()
                print('\n<< 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<삭제 실패!>>\n')
                print(ex)
            
        else:
            print('\n\n<<정보 삭제를 취소했습니다>>\n\n')        


###################################################################################################

# 3. 차량 구매
'''
3-1. 고객 검색 및 선택
3-2. 살수있는 차량 검색 및 선택
3-3. 날짜 추가해서 insert
'''
def Make_Invoice(conn, curs):
    print('\n차량 구매 메뉴입니다\n')
    
    # 차량을 구매한 고객 검색
    print('차량을 구매할 고객을 검색합니다\n')
    idNum = -1
    loop_checker = True
    errChecker = False

    # 고객 검색
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
        
        # 구매 가능한 차량 검색 및 선택
        if idNum != -1 and errChecker == False: 
            print('\n해당 고객을 구매자로 지정합니다\n')
        else:
            print('\n구매를 취소했습니다\n')
        
        # 차량 검색
        print('\n구매할 차량을 검색합니다\n')
        errChecker = False
        print("** 구매 가능 차량 목록 **")
        showSql = "select cl.serial_no, cl.car_model, cl.used, cl.price, s.name, s.phone from car_list cl, Seller s where cl.seller_id= s.seller_id and cl.serial_no not in (select i.car_serial_no from Invoice i, car_list cl where i.car_serial_no = cl.serial_no);"
        Show_DB(curs,showSql)
        
        try:
            loop_checker, resultList = SearchTable(conn, curs, "SELECT cl.serial_no, cl.car_model, cl.used, cl.price, s.name, s.phone from car_list cl left join Seller s  on cl.seller_id=s.seller_id where cl.serial_no not in (select i.car_serial_no from Invoice i, car_list cl2 where i.car_serial_no = cl2.serial_no) and ((convert(cl.serial_no, char) like '%{0}%' or cl.car_model like '%{0}%' or convert(cl.price, char) like '%{0}%' or s.name like '%{0}%' or s.phone like '%{0}%'));",'need type')
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
                    c_idNum = int(input('\n ** 검색 결과 중 해당하는 차량 시리얼 번호(serial_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if c_idNum == -1:
                        break
                    elif c_idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from car_list c where c.serial_no like {}".format(c_idNum))
                    break
                
                except:
                    print('\n<<유효한 값을 입력해 주세요>>\n')
        
        # 검색 데이터가 없는 경우
        elif len(resultList) < 1:
            print('\n<<검색 데이터가 없습니다>>\n')
            errChecker = True
            
        # 검색 결과가 하나인 경우
        else:
            c_idNum = resultList[0][0]

        # 시리얼 넘버, 고객 아이디, 날짜
        # 차량 serial number = c_idNum
        # 고객 id = idNum

        # 날짜 추가해 invoice 테이블에 insert
        now = datetime.now()
        pur_date = now.strftime('%Y-%m-%d')
        try:
            insertSql = "insert into Invoice values({}, {}, '{}');".format(c_idNum, idNum, pur_date)
            curs.execute(insertSql)
            conn.commit()
            print('\n구매 완료!\n')
        except:
            print('invoice insert fail')
        
        try:
            Show_DB(curs,"select * from Invoice where car_serial_no like {}".format(c_idNum))
        except:
            print('show db fail')
        break

###################################################################################################

def Drop_Invoice(conn,cur):
    print('\n구매 정보 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        
        print('** 차량 시리얼 번호로 검색해주세요! **')
        
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Invoice c where convert(c.car_serial_no, char) like '%{0}%';",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 차량 시리얼 번호(car_serial_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Invoice c where c.car_serial_no like {}".format(idNum))
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
            print("\n<<해당 차량에 대한 구매 정보 삭제를 시작합니다>>\n")
            
            try:
                curs.execute("delete from Invoice where car_serial_no={};".format(idNum))
                conn.commit()
                print('\n<< 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<삭제 실패!>>\n')
                print(ex)
            
        else:
            print('\n\n<<정보 삭제를 취소했습니다>>\n\n')



###################################################################################################

# 4. 차량 서비스
# 4-1. 예약 가능 여부 확인
# 4-2. 서비스(예약) 기록 조회 
# 4-3. 서비스(예약) 기록 수정
# 4-4. 서비스(예약) 기록 삭제 
def Service_Car(conn, curs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('차량 수리 서비스 입니다')
    print("""
1. 예약 등록
2. 서비스/예약 기록 조회
3. 서비스/예약 기록 갱신
4. 서비스/예약 기록 삭제
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
        ServiceReg(conn,curs)
        return True
    elif sel == 2:
        # 차량 정보 조회
        ServiceSearch(conn,curs)
        return True
    elif sel == 3:
        # 차량 정보 갱신
        ServiceUpdate(conn,curs)
        return True
    elif sel == 4:
        # 차량 정보 삭제
        ServiceDrop(conn,curs)
        return True
    elif sel == 5:
        # 뒤로가기
        return False
    
    return 0

###################################################################################################
# 4-1 서비스/예약 등록
# 1) 원하는 예약 날짜 입력
# 2) 해당 일자 예약 가능한 목록 출력
# 3) 담당 메카닉 지정 (1명 이상 선택 가능)
# 4) 서비스 예약 확인 
def ServiceReg(conn,curs):
    print('예약 등록 관련 메뉴입니다\n')
    idNum = -1
    loop_checker = True
    errChecker = False
    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select i.car_serial_no, c.name, c.customer_id, i.purchase_date from Invoice i left join Customer c on i.customer_id = c.customer_id where (c.name like '%{0}%' or i.car_serial_no like '%{0}%');",'need type')
            if loop_checker == False:
                raise Exception
        except Exception as ex:
            # 미리 나갈수 있는 분기
            break

        if len(resultList) > 1:
            print('-'*50)
            print('{:^50s}'.format("\n<<결과 내 재검색>> 검색 내용에 중복되는 검색 결과가 존재합니다\n"))
            print('-'*50)
            while True:
                try:
                    idNum = int(input('\n ** 검색 결과 중 해당하는 차량 시리얼 넘버 (car_serial_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select i.car_serial_no, c.name, c.customer_id, i.purchase_date from Invoice i left join Customer c on i.customer_id = c.customer_id where i.car_serial_no={}".format(idNum))
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
        # 서비스 갱신
        if idNum != -1 and errChecker == False:            
            # 실제 등록 메소드 입력 
            # 예약날짜 가능여부
            while True:
                print('예약하고자하는 날짜를 입력해주세요(yyyy-mm-dd 형식)\n')

                try:
                    date = input('날짜 : ')
                    print('====================이용 가능한 메카닉 ====================')
                    searchSql = "select * from Mechanic where mechanic_id not in (select mechanic_id from Service s, Mechanic_Allocation m where s.service_no = m.service_no and service_date='{}');".format(date)
                    print('-'*50)
                    print('{:^50s}'.format("검색 결과"))
                    print('-'*50)
                    resultList = Show_DB(curs,searchSql)
                    print('검색 결과 갯수 : {}\n'.format(len(resultList)))
                    if len(resultList) != 0 :
                        reservation_check = input('해당 일자에 예약하시겠습니까?(y/n) : ')
                        print("고객 정보를 입력해주세요.\n")
                        if reservation_check == 'y':
                            car_serial_no = idNum
                            # 차량번호로 고객 id 가지고 오기
                            curs.execute("select c.customer_id from Invoice i left join Customer c on i.customer_id = c.customer_id where i.car_serial_no={}".format(car_serial_no))  
                            result = curs.fetchall()
                            service_no = idNum
                            customer_id = result[0][0]
                            insertSql = "insert into Service(car_serial_no, customer_id, service_date) values('{}','{}','{}');".format(car_serial_no, customer_id, date)
                            curs.execute(insertSql)
                            conn.commit()
                            print('\n등록되었습니다!\n')
                            service_no = Get_Inserted_id(curs)
                            Show_DB(curs,"select s.service_no, c.customer_id, c.name, s.car_serial_no from Service s left join Customer c on s.customer_id = c.customer_id where s.service_no={} and s.car_serial_no={}".format(service_no, car_serial_no))
                            break
                    else:
                        print('{} 일자에 예약이 가득 찼습니다.\n\n'.format(date))
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
            print('서비스에 지정될 메카닉을 입력해주세요\n')

            try:
                mechanic_ids = input('Mechanic ID(여러명 입력시 \',\'로 구분) : ')
                id_list = mechanic_ids.split(',')
                insertSql = "insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values ('{}','{}','{}');"
                for mid in id_list:    
                    curs.execute(insertSql.format(service_no, car_serial_no, mid))
                    conn.commit()
                print('\n메카닉 추가 완료!\n')    
                Show_DB(curs, "select * from Mechanic_Allocation where service_no='{}';".format(service_no))
            except:
                print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
    

    return 0
###################################################################################################
# 4-2 서비스(예약) 기록 조회 
def ServiceSearch(conn,curs):
    print('<<조회 메뉴를 선택하세요>>')
    print("""
1. 전체 서비스 기록 조회
2. 서비스 부품 사용 상세 조회
3. 서비스 담당 메카닉 상세 조회
4. 종료""")

    while True:
        try:
            sel = int(input('메뉴 번호를 선택해주세요 : '))
            if sel != 1 and sel != 2 and sel != 3 and sel !=4:
                raise Exception
            else:
                break

        except:
            print('유효한 값을 입력해주세요')
    if sel == 1:
        # 1. 전체 서비스 기록 조회
        selectSql="select s.service_no, c.name, c.phone, s.car_serial_no, s.service_date from Service s, Customer c where c.customer_id=s.customer_id;"        
        Show_DB(curs, selectSql)
        return True
    elif sel == 2:
        # 2. 서비스 부품 사용 상세 조회
        service_no = input('서비스 번호 : ')
        selectSql="select s.service_no, s.car_serial_no, c.name, c.phone, p.name as 'parts', s.service_date from Service s, Customer c, Parts_requirement pr, Parts p where c.customer_id=s.customer_id and s.service_no=pr.service_no and p.parts_no=pr.parts_no and s.service_no={};"
        Show_DB(curs, selectSql.format(service_no))
        return True
    elif sel == 3:
        # 3. 서비스 담당 메카닉 상세 조회
        service_no = input('서비스 번호 : ')
        selectSql="select s.service_no, s.car_serial_no, c.name, c.phone, m.name as 'mechanic', s.service_date from Service s, Customer c, Mechanic_Allocation ma, Mechanic m where c.customer_id=s.customer_id and s.service_no=ma.service_no and m.mechanic_id =ma.mechanic_id and s.service_no={};"
        Show_DB(curs, selectSql.format(service_no))
        return True
    elif sel == 4:
        # 뒤로가기
        return False
    return 0
###################################################################################################
# 4-3 서비스(예약) 기록 갱신
# 1) 서비스 리스트 출력 후 변경하고자 하는 서비스 확인
#    1-1) 서비스 날짜 수정
# 2) 상세 서비스 수정
#    2-1) 메카닉 추가
#       - 사용가능한 메카닉 리스트 출력        
#    2-2) 메카닉 변경
#       - 사용가능한 메카닉 리스트 출력
#    2-3) 파츠 추가
#       - 사용가능한 파츠 리스트 출력
#    2-4) 파츠 변경
#       - 사용가능한 파츠 리스트 출력
def ServiceUpdate(conn,curs):
    print('\t서비스/예약 갱신 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False
    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select s.service_no, s.car_serial_no,  c.customer_id, c.name, s.service_date from Service s, Customer c where s.customer_id=c.customer_id and ( s.service_no like '%{0}%' or c.name like '%{0}%' or s.car_serial_no like '%{0}%');",'need type')
            if loop_checker == False:
                raise Exception
        except Exception as ex:
            # 미리 나갈수 있는 분기
            break

        if len(resultList) > 1:
            print('-'*50)
            print('{:^50s}'.format("\n<<결과 내 재검색>> 검색 내용에 중복되는 검색 결과가 존재합니다\n"))
            print('-'*50)
            while True:
                try:
                    idNum = int(input('\n ** 검색 결과 중 해당하는 서비스 넘버 (service_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select s.service_no, s.car_serial_no,  c.customer_id, c.name, s.service_date from Service s, Customer c where s.customer_id=c.customer_id and service_no={}".format(idNum))
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
        # 서비스 갱신
        if idNum != -1 and errChecker == False:            
            #실제 갱신 메소드 입력 
            curs.execute('select car_serial_no from Service where service_no={};'.format(idNum))  
            result = curs.fetchall()
            service_no = idNum
            car_serial_no = result[0][0]
            
            #####
            print('\n<<갱신 메뉴를 선택하세요>>')
            print("""
1. 서비스/예약 날짜 변경
2. 담당 메카닉 추가
3. 담당 메카닉 변경
4. 사용 파츠 추가
5. 사용 파츠 변경
6. 종료""")

            while True:
                try:
                    sel = int(input('메뉴 번호를 선택해주세요 : '))
                    if sel != 1 and sel != 2 and sel != 3 and sel !=4 and sel !=5 and sel !=6:
                        raise Exception
                    else:
                        break

                except:
                    print('유효한 값을 입력해주세요')

            if sel == 1:
                # 1. 서비스/예약 날짜 변경
                print('변경하고자하는 날짜를 입력해주세요(yyyy-mm-dd 형식)\n')

                try:
                    date = input('날짜 : ')
                    searchSql = "select * from Mechanic where mechanic_id not in (select mechanic_id from Service s, Mechanic_Allocation m where s.service_no = m.service_no and service_date='{}');".format(date)
                    resultList = Show_DB(curs,searchSql)
                    print('검색 결과 갯수 : {}\n'.format(len(resultList)))
                    if len(resultList) != 0 :
                        reservation_check = input('해당 일자로 변경하시겠습니까?(y/n) : ')
                        if reservation_check == 'y':
                            updateSql = "update Service SET service_date='{}' where service_no={};".format(date, service_no)
                            curs.execute(updateSql)
                            conn.commit()
                            print('\n변경되었습니다!\n')
                            selectSql="select s.service_no, c.name, c.phone, s.car_serial_no, s.service_date from Service s, Customer c where c.customer_id=s.customer_id where serivce_no={};"        
                            Show_DB(curs, selectSql.format(service_no))   
                    else:
                        print('{} 일자에 예약이 가득 찼습니다.\n\n'.format(date))
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
                return True
            elif sel == 2:
                # 2. 담당 메카닉 추가
                try:
                    searchSql = "select * from Mechanic where mechanic_id not in (select mechanic_id from Service s, Mechanic_Allocation m where s.service_no = m.service_no and service_no='{}');".format(service_no)
                    resultList = Show_DB(curs,searchSql)
                    print('검색 결과 갯수 : {}\n'.format(len(resultList)))
                    if len(resultList) != 0 :
                        mid = input('메카닉 ID : ')
                        reservation_check = input('해당 메카닉을 추가하시겠습니까?(y/n) : ')
                        if reservation_check == 'y':
                            insertSql = "insert into Mechanic_Allocation  values ({}, {} ,{});".format(service_no, car_serial_no, mid)
                            curs.execute(insertSql)
                            conn.commit()
                            print('\n메카닉이 추가되었습니다!\n')
                            selectSql="select s.service_no, s.car_serial_no, c.name, c.phone, m.name as 'mechanic', s.service_date from Service s, Customer c, Mechanic_Allocation ma, Mechanic m where c.customer_id=s.customer_id and s.service_no=ma.service_no and m.mechanic_id =ma.mechanic_id and s.service_no={};"
                            Show_DB(curs, selectSql.format(service_no)) 
                    else:
                        print('{} 일자에 예약이 가득 찼습니다.\n\n'.format(date))
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
                return True
            elif sel == 3:
                # 3. 담당 메카닉 변경
                print('===============현재 지정된 메카닉 List===============')
                searchSql = "select * from Mechanic_Allocation where service_no={}".format(service_no)
                resultList = Show_DB(curs,searchSql)
                searchSql2 = "select * from Mechanic where mechanic_id not in (select mechanic_id from Service s, Mechanic_Allocation m where s.service_no = m.service_no and s.service_no={});".format(service_no)
                print('===============선택 가능한 메카닉 List===============')
                resultList = Show_DB(curs,searchSql2)
                try:    
                    if len(resultList) != 0 :
                        mid = input('변경 전 메카닉 ID : ')
                        new_mid = input('변경 후 메카닉 ID : ')
                        reservation_check = input('해당 메카닉을 변경하시겠습니까?(y/n) : ')
                        if reservation_check == 'y':
                            updateSql = "update Mechanic_Allocation set mechanic_id={} where service_no={} and mechanic_id={};".format(new_mid, service_no, mid) 
                            curs.execute(updateSql)
                            conn.commit()
                            print('\n메카닉이 변경되었습니다!\n')
                            selectSql="select s.service_no, s.car_serial_no, c.name, c.phone, m.name as 'mechanic', s.service_date from Service s, Customer c, Mechanic_Allocation ma, Mechanic m where c.customer_id=s.customer_id and s.service_no=ma.service_no and m.mechanic_id =ma.mechanic_id and s.service_no={};"
                            Show_DB(curs, selectSql.format(service_no)) 
                    else:
                        print('{} 일자에 예약이 가득 찼습니다.\n\n'.format(date))
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
                return True
            elif sel == 4:
                # 4. 사용 파츠 추가
                # 사용 가능한 파츠 표시
                selectSql="select * from Parts where parts_no not in (select pr.parts_no from Service s, Parts_requirement pr where s.service_no=pr.service_no and s.service_no={});".format(service_no)
                print('======================추가 가능한 Parts List==========================')
                Show_DB(curs, selectSql)
                pno = input("파츠 넘버(parts_no) : ")
                insertSql = "insert into Parts_requirement(service_no, car_serial_no, parts_no) values ({}, {}, {});".format(service_no, car_serial_no, pno) 
                curs.execute(insertSql)
                conn.commit()
                print('=====================현재 사용 중인 파츠 목록==========================')
                selectSql="select * from Parts_requirement where service_no={};".format(service_no)
                Show_DB(curs, selectSql)
                return True
            elif sel == 5:
                # 5. 사용 파츠 변경
                # 사용 중인 파츠
                print('======================사용 중인 Parts List==========================')
                selectSql="select * from Parts_requirement where service_no={};".format(service_no)
                Show_DB(curs, selectSql)
                # 사용 가능한 파츠 
                print('======================사용 가능한 Parts List==========================')
                canUseSql="select * from Parts where parts_no not in (select pr.parts_no from Service s, Parts_requirement pr where s.service_no=pr.service_no and s.service_no={});".format(service_no)
                Show_DB(curs, canUseSql)
                pno = input("변경 전 파츠 넘버(parts_no) : ")
                new_pno = input("변경 후 파츠 넘버(parts_no) : ")
                updateSql="update Parts_requirement set parts_no={} where service_no={} and parts_no={};".format(pno,service_no,new_pno)
                curs.execute(updateSql)
                conn.commit()
                return True
            elif sel == 6:
                # 뒤로가기
                return False            

        else:
            print('\n\n<<업데이트를 취소했습니다>>\n\n')

    return 0
###################################################################################################
# 4-4 서비스(예약) 기록 삭제
# 1) 서비스 삭제
# 2) 부품(Parts_Requirement 삭제)
# 3) 메카닉 지정 해제 (Mechanic_Allocation) 
def ServiceDrop(conn,curs):

    print('\t서비스/예약 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False
    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select s.service_no, s.car_serial_no,  c.customer_id, c.name, s.service_date from Service s, Customer c where s.customer_id=c.customer_id and ( s.service_no like '%{0}%' or c.name like '%{0}%' or s.car_serial_no like '%{0}%');",'need type')
            if loop_checker == False:
                raise Exception
        except Exception as ex:
            # 미리 나갈수 있는 분기
            break

        if len(resultList) > 1:
            print('-'*50)
            print('{:^50s}'.format("\n<<결과 내 재검색>> 검색 내용에 중복되는 검색 결과가 존재합니다\n"))
            print('-'*50)
            while True:
                try:
                    idNum = int(input('\n ** 검색 결과 중 해당하는 서비스 넘버 (service_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select s.service_no, s.car_serial_no,  c.customer_id, c.name, s.service_date from Service s, Customer c where s.customer_id=c.customer_id and service_no={}".format(idNum))
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
        # 서비스 삭제 
        if idNum != -1 and errChecker == False:            
            #실제 삭제 메소드 입력 
            curs.execute('select car_serial_no from Service where service_no={};'.format(idNum))  
            result = curs.fetchall()
            service_no = idNum
            
            #####
            print('\n<<삭제 메뉴를 선택하세요>>')
            print("""
            1. 서비스/예약 삭제
            2. 사용 파츠 제거
            3. 담당 메카닉 사용 삭제
            4. 종료""")

            while True:
                try:
                    sel = int(input('메뉴 번호를 선택해주세요 : '))
                    if sel != 1 and sel != 2 and sel != 3 and sel !=4:
                        raise Exception
                    else:
                        break

                except:
                    print('유효한 값을 입력해주세요')

            if sel == 1:
                # 서비스 삭제 
                ch = input('Service를 정말 삭제하시겠습니까?(y/n) : ')
                if ch == 'y':
                    deleteSql = "delete from Service where service_no={}".format(service_no)
                    curs.execute(deleteSql)
                    conn.commit()
                return True
            elif sel == 2:
                # 2. 사용 부품 삭제
                try:
                    print('======================사용 중인 Parts List==========================')
                    selectSql="select * from Parts_requirement where service_no={};".format(service_no)
                    resultList = Show_DB(curs, selectSql)
                    
                    print('검색 결과 갯수 : {}\n'.format(len(resultList)))
                    if len(resultList) != 0 :
                        pno = input("삭제할 파츠 넘버(parts_no) : ")
                        reservation_check = input('해당 메카닉을 제거하시겠습니까?(y/n) : ')
                        if reservation_check == 'y':
                            deleteSql = "delete from Parts_requirement where parts_no = {};".format(pno)
                            curs.execute(deleteSql)
                            conn.commit()
                            print('\n{}번 메카닉이 삭제 되었습니다!\n'.format(pno))
                            print('===============삭제 후 지정된 메카닉 List===============')
                            searchSql = "select * from Mechanic_Allocation where service_no={}".format(service_no)
                            resultList = Show_DB(curs,searchSql)
                    else:
                        print('사용된 파츠 없습니다.')
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
                return True
            elif sel == 3:
                # 3. 담당 메카닉 삭제
                try:
                    print('===============현재 지정된 메카닉 List===============')
                    searchSql = "select * from Mechanic_Allocation where service_no={}".format(service_no)
                    resultList = Show_DB(curs,searchSql)
                    print('검색 결과 갯수 : {}\n'.format(len(resultList)))
                    if len(resultList) != 0 :
                        mid = input('메카닉 ID : ')
                        reservation_check = input('해당 메카닉을 제거하시겠습니까?(y/n) : ')
                        if reservation_check == 'y':
                            deleteSql = "delete from Mechanic_Allocation where mechanic_id = {};".format(mid)
                            curs.execute(deleteSql)
                            conn.commit()
                            print('\n{}번 메카닉이 삭제 되었습니다!\n'.format(mid))
                            print('===============삭제 후 지정된 메카닉 List===============')
                            searchSql = "select * from Mechanic_Allocation where service_no={}".format(service_no)
                            resultList = Show_DB(curs,searchSql)
                    else:
                        print('지정된 메카닉이 없습니다.')
                except:
                    print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')
                return True
            elif sel == 4:
                # 뒤로가기
                return False            

        else:
            print('\n\n<<삭제를 취소했습니다>>\n\n')
    return 0


###################################################################################################
# 7. Parts CRUD
def CRUD_Parts(conn, curs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('부품 관련 메뉴입니다')
    print("""

1. 부품 등록

2. 부품 정보 조회

3. 부품 정보 갱신

4. 부품 정보 삭제

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
        # 파츠 등록
        PartsReg(conn, curs)
        return True
    elif sel == 2:
        # 파츠 정보 조회
        PartsSearch(conn,curs)
        return True
    elif sel == 3:
        # 파츠 정보 갱신
        PartsUpdate(conn,curs)
        return True
    elif sel == 4:
        # 파츠 정보 삭제
        PartsDrop(conn,curs)
        return True
    elif sel == 5:
        # 뒤로가기
        return False

    return 0

##################################################################################################

# 7-1 파츠 등록
# insert into Parts(price, name) values (200, 'Air Filter');
def PartsReg(conn, curs):
    print('파츠 등록 관련 메뉴입니다\n')
    while True:
        print('등록할 파츠 정보를 입력해주세요\n')

        try:
            price = input('가격 : ')
            pName = input("Parts 이름 : ")
            insertSql = "insert into Parts(price, name) values ({}, '{}')".format(price, pName);
            curs.execute(insertSql)
            conn.commit()
            print('\n등록되었습니다!\n')
            Show_DB(curs,"select * from Parts where price like '{}' and name like '{}';".format(price, pName))
            break
        except:
            print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')

##################################################################################################

# 7-2 파츠 정보 조회

def PartsSearch(conn, curs):
    print('파츠 검색 관련 메뉴입니다\n')
    loop_checker = True
    while loop_checker:
        loop_checker, ls = SearchTable(conn, curs, "select * from Parts where name like '%{0}%' or parts_no like '%{0}%';",'need type')

##################################################################################################
# 7-3 고객 정보 갱신

def PartsUpdate(conn, curs):
    print('\n파츠 정보 갱신 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Parts where name like '%{0}%' or parts_no like '%{0}%';",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 Parts Number (parts_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Parts  where parts_no={}".format(idNum))
                    break
                
                except:
                    print('\n<<유효한 값을 입력해 주세요>>\n')
        
        # 파츠 데이터가 없는 경우
        elif len(resultList) < 1:
            print('\n<<검색 데이터가 없습니다>>\n')
            errChecker = True

        # 파츠 결과가 하나인 경우
        else:
            idNum = resultList[0][0]

        # 파츠 정보 갱신 부분 (name, phone, address, e_mail)
        if idNum != -1 and errChecker == False:
            print("\n<<해당 고객에 대한 파츠 정보 갱신을 시작합니다>>\n")
            while True:
                try:
                    pName = input('이름 : ')
                    pPrice = input('가격 : ')
                    break
                except:
                    print("\n<<유효한 값을 입력하세요>>\n")
            try:
                curs.execute("update Parts set name='{}',price='{}' where parts_no={}".format(pName,pPrice,idNum))
                conn.commit()

                Show_DB(curs,"select * from Parts where parts_no={}".format(idNum))
                print('\n<<업데이트 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<업데이트에 실패했습니다>>\n')
                print(ex)
            
        else:
            print('\n\n<<업데이트를 취소했습니다>>\n\n')


##################################################################################################
# 7-4 파츠 정보 삭제

def PartsDrop(conn,curs):
    print('\n파츠 정보 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Parts where name like '%{0}%' or parts_no like '%{0}%';",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 Parts Number (parts_no)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Parts  where parts_no={}".format(idNum))
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
            print("\n<<해당 고객에 대한 정보 삭제를 시작합니다>>\n")
            
            try:
                curs.execute("delete from Parts where parts_no={};".format(idNum))
                conn.commit()
                print('\n<< 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<삭제 실패!>>\n')
                print(ex)
            
        else:
            print('\n\n<<정보 삭제를 취소했습니다>>\n\n')

###################################################################################################
# 8. Mechanic CRUD
def CRUD_Mechanic(conn, curs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('정비공 관련 메뉴입니다')
    print("""

1. 정비공 등록

2. 정비공 정보 조회

3. 정비공 정보 갱신

4. 정비공 정보 삭제

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
        # 정비공 등록
        MechanicReg(conn, curs)
        return True
    elif sel == 2:
        # 정비공 정보 조회
        MechanicSearch(conn,curs)
        return True
    elif sel == 3:
        # 정비공 정보 갱신
        MechanicUpdate(conn,curs)
        return True
    elif sel == 4:
        # 정비공 정보 삭제
        MechanicDrop(conn,curs)
        return True
    elif sel == 5:
        # 뒤로가기
        return False

    return 0

##################################################################################################

# 8-1 메카닉 등록
# insert into Mechanic (name, phone, major, store) values('Lyon', '010-1111-0000', 'Computer Science', 'Jamsil');
def MechanicReg(conn, curs):
    print('정비공 등록 관련 메뉴입니다\n')
    while True:
        print('등록할 정비공 정보를 입력해주세요\n')

        try:
            mName = input('이름 : ')
            mPhone = input("전화번호('-'를 포함) : ")
            mMajor = input('전공 : ')
            mStore = input("지점명 : ")
            insertSql = "insert into Mechanic (name, phone, major, store) values('{}', '{}', '{}', '{}');".format(mName, mPhone, mMajor, mStore)
            curs.execute(insertSql)
            conn.commit()
            print('\n등록되었습니다!\n')
            Show_DB(curs,"select * from Mechanic where name like '{}' and phone like '{}' and major like '{}' and store like '{}';".format(mName, mPhone, mMajor, mStore))
            break
        except:
            print('\n유효한 값을 입력해주세요 (45자 이내로 써주세요)\n')

##################################################################################################

# 8-2 메카닉 정보 조회

def MechanicSearch(conn, curs):
    print('정비공 검색 관련 메뉴입니다\n')
    loop_checker = True
    while loop_checker:
        loop_checker, ls = SearchTable(conn, curs, "select * from Mechanic where name like '%{0}%' or phone like '%{0}%' or store like '%{0}%' or major like '%{0}%';",'need type')

##################################################################################################
# 8-3 메카닉 정보 갱신

def MechanicUpdate(conn, curs):
    print('\n정비공 정보 갱신 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Mechanic where name like '%{0}%' or phone like '%{0}%' or store like '%{0}%' or major like '%{0}%';",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 정비공 ID (mechanic_id)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Mechanic  where mechanic_id={}".format(idNum))
                    break
                
                except:
                    print('\n<<유효한 값을 입력해 주세요>>\n')
        
        # 정비공 데이터가 없는 경우
        elif len(resultList) < 1:
            print('\n<<검색 데이터가 없습니다>>\n')
            errChecker = True

        # 정비공 결과가 하나인 경우
        else:
            idNum = resultList[0][0]

        # 정비공 정보 갱신 부분 (name, phone, address, e_mail)
        if idNum != -1 and errChecker == False:
            print("\n<<해당 고객에 대한 정비공 정보 갱신을 시작합니다>>\n")
            while True:
                try:
                    mName = input('이름 : ')
                    mPhone = input("전화번호('-'를 포함) : ")
                    mMajor = input('전공 : ')
                    mStore = input("지점명 : ")
                    break
                except:
                    print("\n<<유효한 값을 입력하세요>>\n")
            try:
                curs.execute("update Mechanic set name='{}',phone='{}', major='{}', store='{}' where mechanic_id={}".format(mName, mPhone, mMajor, mStore, idNum))
                conn.commit()

                Show_DB(curs,"select * from Mechanic where mechanic_id={}".format(idNum))
                print('\n<<업데이트 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<업데이트에 실패했습니다>>\n')
                print(ex)
            
        else:
            print('\n\n<<업데이트를 취소했습니다>>\n\n')


##################################################################################################
# 8-4 메카닉 정보 삭제

def MechanicDrop(conn,curs):
    print('\n메카닉 정보 삭제 메뉴입니다\n')
    
    idNum = -1
    loop_checker = True
    errChecker = False

    while loop_checker:
        try:
            loop_checker, resultList = SearchTable(conn, curs, "select * from Mechanic where name like '%{0}%' or phone like '%{0}%' or store like '%{0}%' or major like '%{0}%';",'need type')
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
                    idNum = int(input('\n ** 검색 결과 중 해당하는 Mechanic ID (mechanic_id)를 입력해주세요, 없다면 -1을 입력해 주세요 : '))
                    if idNum == -1:
                        break
                    elif idNum in [resultList[i][0] for i in range(len(resultList))]:
                        pass
                    else:
                        raise Exception
                    
                    resultList = Show_DB(curs,"select * from Mechanic  where mechanic_id={}".format(idNum))
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
        
        # 정비공 삭제 부분
        if idNum != -1 and errChecker == False:
            print("\n<<해당 정비공에 대한 정보 삭제를 시작합니다>>\n")
            
            try:
                curs.execute("delete from Mechanic where mechanic_id={};".format(idNum))
                conn.commit()
                print('\n<< 성공!>>\n')
                break
            except Exception as ex:
                print('\n<<삭제 실패!>>\n')
                print(ex)
            
        else:
            print('\n\n<<정보 삭제를 취소했습니다>>\n\n')

###################################################################################################

# Database Connect Function
def DB_Connection(host:str, port:int, user:str, password:str, db:str, charset:str):
    con = pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
    return con, con.cursor()

###################################################################################################
# Get id of Latest Inserted element
def Get_Inserted_id(curs):
    curs.execute('SELECT LAST_INSERT_ID();')  
    result = curs.fetchall()
    return result[0][0]


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
        keyword = input("검색어 (종료를 원할시 'exit'를 입력해주세요) : ")
        if keyword == 'exit':
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
# dbName = input('데이터베이스 이름 입력 : ')
#con, curs = DB_Connection('localhost',3306,'root','password','car_test','utf8')
con, curs = DB_Connection('dealership',3306,'root','','car_test','utf8')
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