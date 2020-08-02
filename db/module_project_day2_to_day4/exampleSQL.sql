/*1. 고객 Create*/
 insert into Customer (name, phone, address, e_mail) values('Arron', '010-0000-0000', 'seoul', 'arron@abc.com');

/*2. 고객 Read */

/*전체 고객 조회*/
select * from Customer;

/*전체 고객 구매(보유) 차량 조회*/
select d.serial_no, d.car_model, c.name
from Customer c left join 
(select * from Invoice i left join car_list cl on cl.serial_no=i.car_serial_no) as d
on c.customer_id = d.customer_id

/*고객 정보(id, 이름, 전화번호, 메일)별로 차량 조회*/
select d.serial_no, d.car_model, c.name
from Customer c left join (select * from Invoice i left join car_list cl on cl.serial_no=i.car_serial_no) as d on c.customer_id = d.customer_id
where c.customer_id = @var or c.name=@var or c.phone=@var or c.e_mail=@var;

/*전체 고객 서비스 기록 조회*/
 select c.customer_id, c.name, s.service_no, s.service_date
 from Customer c, Service s
 where c.customer_id = s.customer_id
 order by c.name;

 /*고객 정보(id, 이름, 전화번호, 메일)별로 서비스 기록 조회 *//*select @var :='Jenny'; */
 select *
 from Customer c left join Service s on c.customer_id = s.customer_id
 where c.customer_id like '%@var%' or c.name like '%@var%' or c.phone like '%@var%' or c.e_mail like '%@var%';

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
                update Customer set(name,phone,address,e_mail) values() where customer_id=1; 
        - D
            - 고객 정보 삭제 
                # delete from Customer where customer_id=11;