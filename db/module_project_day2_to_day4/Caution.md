# 변경사항 및 논의 내용

## Car CRUD 부분

### Car Create

```
insert into car_list(seller_id, car_model, used, price) values(1,'Santafe', False, 42000 );
```
여기서 굳이 seller_id를 넣어줘야 하는지 모르겠음 --> auto increase 상태면 빼도 상관 없는것 아닌지 

### Car Read

```
select cl.serial_no, cl.car_model, cl.price, s.name as 'Seller Name', s.phone, s.store from car_list cl left join Seller s on cl.seller_id =s.seller_id where cl.serial_no='' or cl.car_model='' or cl.price='' or s.name='' or s.phone='' or s.store='' order by s.name;
```
각 attribute 별 자료형 확인