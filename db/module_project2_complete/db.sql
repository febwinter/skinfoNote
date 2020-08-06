/*
    1. 고객 관리
        - C 
            - 고객 추가 
                # insert into Customer (name, phone, address, e_mail) values('', '', '', '');
        - R
            - 전체 고객 출력
                # select * from Customer;
            - 검색 고객 출력 (Like)
                # select *
                  from Customer 
                  where customer_id = @var or name=@var or phone=@var or e_mail=@var;
        - U
            - 고객 정보 수정
                # update Customer SET name='' where customer_id=1;
                # update Customer SET phone='' where customer_id=1;
                # update Customer SET address='' where customer_id=1;
                # update Customer SET e_mail='' where customer_id=1;
        - D
            - 고객 정보 삭제 
                # delete from Customer where customer_id=11;
    2. 차량 관리
        - C
            - 차량 정보 추가
                #3 insert into car_list(seller_id, car_model, used, price) values(1,'Santafe', False, 42000 );
        - R 
            - Car List(시리얼넘버, 차량 모델명, 중고여부, 가격, 판매자, 구매자이름)
                # select cl.serial_no, cl.car_model, cl.price, s.name, s.phone, s.store
                  from car_list cl, Seller s
                  where cl.seller_id =s.seller_id
                  order by s.name;

                select * from car_list where convert(serial_no, char) like '%23%';

            - 검색 차량 출력 (Like) - 조건별 수정
                # select cl.serial_no, cl.car_model, cl.price, s.name as 'Seller Name' , s.phone, s.store
                  from car_list cl left join Seller s on cl.seller_id =s.seller_id
                  where cl.serial_no='' or cl.car_model='' or cl.price='' or s.name='' or s.phone='' or s.store=''
                  order by s.name;
        - U
            - 차량 정보 수정
                # update car_list SET seller_id='' where serial_no=1;
                # update car_list SET used='' where serial_no=1;
                # update car_list SET price='' where serial_no=1;
        - D
            - 차량 정보 삭제 
                # delete from car_list where serial_no=11;
    3. 차량 구매 (Invoice)
        - C
            - 구매 정보 추가 
                # insert into Invoice values(차량 시리얼넘버, 고객 ID, 구매 날짜);
        - R 
            - Car List(시리얼넘버, 차량 모델명, 중고여부, 가격, 판매자, 구매자이름, Purchase Date)
                # select cl.serial_no, cl.car_model, cl.used, cl.price, s.name as 'Seller', s.phone, i.purchase_date
                  from car_list cl, Seller s, Invoice i
                  where cl.seller_id =s.seller_id and cl.serial_no=i.car_serial_no
                  order by s.name;
        - U 
            - 구매내역에 대해서 수정 사항이 필요 없을거 같음.
        - D
            - 구매 내역 삭제
                # delete from  Invoice where car_serial_no='';
    4. 차량 서비스 
        - C 
            예약 가능 여부 확인
            1. 고객이 원하는 날짜를 입력
            2. 예약 가능한 메카닉 목록 (아무도 없으면 다시 날짜 입력화면으로 이동 )
                # select *
                  from Mechanic
                  where mechanic_id not in (
                        select mechanic_id
                        from Service s, Mechanic_Allocation m
                        where s.service_no = m.service_no
                        and service_date='2020-08-13');
            3. 담당 메카닉 지정 (한명 이상 지정 가능)
                - 1) 서비스 생성(차량시리얼넘버, 고객id, 서비스(예약)일자)
                    # insert into Service(car_serial_no, customer_id, service_date) values (1000245, 5,'2020-08-20');
                - 2) service_no 확인
                    # SELECT LAST_INSERT_ID();
                - 3) 메카닉 지정 (여러명일 경우 쿼리 여러번 실행)
                    # insert into Mechanic_Allocation(service_no, car_serial_no, mechanic_id)  values ('서비스넘버','차량시리얼넘버','메카닉아이디');
            4. 서비스 예약 확인 
                # select s.service_no, s.car_serial_no, c.name, c.phone, m.name, s.service_date
                  from Service s, Customer c, Mechanic_Allocation ma, Mechanic m
                  where c.customer_id=s.customer_id and s.service_no=ma.service_no and m.mechanic_id =ma.mechanic_id
                  and s.service_no='서비스넘버';
        - R
            - 전체 서비스 기록 조회
                # select s.service_no, c.name, c.phone, s.car_serial_no, s.service_date
                  from Service s, Customer c
                  where c.customer_id=s.customer_id;
            - service_no를 통해 상세 조회
                - 서비스 + 부품 
                    # select s.service_no, s.car_serial_no, c.name, c.phone, p.name, s.service_date
                      from Service s, Customer c, Parts_requirement pr, Parts p
                      where c.customer_id=s.customer_id and s.service_no=pr.service_no and p.parts_no=pr.parts_no
                      and s.service_no=10;
                - 서비스 + 엔지니어 
                    # select s.service_no, s.car_serial_no, c.name, c.phone, m.name, s.service_date
                      from Service s, Customer c, Mechanic_Allocation ma, Mechanic m
                      where c.customer_id=s.customer_id and s.service_no=ma.service_no and m.mechanic_id =ma.mechanic_id
                      and s.service_no=10;
        - U
            - Service 정보 수정 
                - 서비스(예약) 날짜 수정
                    - service_date 
                        # update Service SET service_date='' where service_no=1;
                - 서비스 고객 수정
                    - customer_id 
                        # update Service SET customer_id='' where service_no=1;
            - 상세 service 수정
                - 담당 Mechanic 추가
                    # insert into Mechanic_Allocation  values ('서비스넘버', '차량시리얼넘버','메카닉 번호');
                - 담당 Mechanic 변경
                    # update Mechanic_Allocation set mechanic_id='새로운 메카닉' where service_no='수정할 서비스' and mechanic_id='수정할 메카닉'; 
                - 사용 Parts 추가 
                    # insert into Parts_requirement(service_no, car_serial_no, parts_no) values ('서비스넘버', '차량 시리얼넘버', '파츠 번호');
                - 사용 Parts 변경
                    # update Parts_requirement set parts_no='새로운 파츠' where service_no='수정할 서비스' and parts_no='수정할 파츠'; 
        - D
            - Service 삭제
                - service_no를 통해서 삭제
                    # delete from Service where service_no=42;
                - 연결된 Part_requirement, Mechanic_Allocation도 삭제 해야함
                    => CASCADE 속성을 부여해서 해당 두 테에블에 연관된 값도 자동으로 삭제
            - Service 부품 삭제
                - Parts-requirement의 Parts_no를 통해 삭제
                    # delete from Parts_requirement where parts_no = 10;
            - Service Mechanic 삭제
                - Mechanic_Allocation의 mechanic_id를 통해서 삭제
                    # delete from Mechanic_Allocation where mechanic_id = 2;
    5. 부품 관리
        - C
            - 새로운 부품 추가
                # insert into Parts(price, name) values (200, 'Air Filter');
        - R 
            - 부품 리스트 확인
                # select * from Parts
        - U
            - 부품 가격 수정
                # update Parts set(변경할 항목) = (변경하고자하는 값) where parts_no='파츠번호';
        - D
            - 부품 삭제 
                # delete from Parts where parts_no='파츠번호';
    6. 메카닉 관리
        - C
            - 메카닉 추가
                # insert into Mechanic (name, phone, major, store) values('이름', '전화번호 - 포함', '전공', '지점');
        - R
            - 메카닉 리스트 확인
                # select * from Mechanic
        - U
            - 메카닉 정보 수정
                # update Mechanic set(변경할 항목) = (변경하고자하는 값) where mechanic_id='메카닉번호';
        - D       
            - 메카닉 삭제 
                # delete from Mechanic where mechanic_id='메카닉번호';



*/

