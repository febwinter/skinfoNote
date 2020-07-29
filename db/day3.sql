#SELECT SUBSTR(NAME,1,1) AS '성', COUNT(*) '인원'
#FROM Customer
#GROUP BY SUBSTR(NAME,1,1);


# SELECT orderid '주문번호', orderdate '주문일',
# 		adddate(orderdate, interval 10 DAY) '확정'
# from Orders;

# SELECT orderid '주문번호', DATE_FORMAT(orderdate, '%y-%M-%d') '주문일',
#			custid '고객번호', bookid '도서번호'
# FROM Orders
# WHERE orderdate=DATE_FORMAT('20140707', '%Y%m%d');

# SELECT NAME,
# 			IFNULL(phone,'연락처없음') '전화번호'
# FROM Customer;

# SELECT Orders.custid, NAME, SUM(saleprice)
# from Orders, Customer
# WHERE Orders.custid = Customer.custid
# GROUP BY Orders.custid

# SELECT custid, (SELECT NAME FROM Customer AS c
#						WHERE c.custid = o.custid) AS custname,
#						SUM(saleprice) # 반환값이 하나뿐인 스칼라 서브쿼리
#FROM Orders o
#GROUP BY custid;

# SELECT *, (SELECT bookname 
# 				FROM Book 
# 				WHERE Book.bookid = Orders.bookid) AS '책 제목'
# FROM Orders;

# SELECT NAME, SUM(saleprice) 'total'
# FROM (SELECT custid, NAME # inline view
# 		FROM Customer
# 		WHERE custid <= 2) c, Orders o
# WHERE c.custid = o.custid
# GROUP BY name

# CREATE VIEW vBook
# AS
# SELECT * 
# FROM Book
# WHERE Book.bookname LIKE '%축구%';

# SELECT *
# FROM vBook;

#CREATE VIEW vw_Orders (orderid, custid, NAME, bookid, bookname, saleprice, orderdate)
#AS SELECT od.orderid, od.custid, cs.name, od.bookid, bk.bookname, od.saleprice, od.orderdate
#	FROM Orders od, Customer cs, Book bk
#	WHERE od.custid = cs.custid AND od.bookid = bk.bookid;
	
# SELECT *
# FROM vw_Orders;	 

# CREATE VIEW vCustomer
# AS SELECT custid, NAME, address, phone
# 	FROM Customer
# 	WHERE address LIKE '대한민국%';
	
# SELECT * FROM vCustomer;

# CREATE OR REPLACE VIEW vCustomer(custid, NAME, address)
# AS SELECT custid, NAME , address
# 	FROM Customer
# 	WHERE address LIKE '영국%';

# SELECT * FROM vCustomer;

# 고객별 주문합계를 나타내는 view (vOrder Total)

# CREATE or replace VIEW vOrder
# AS
# SELECT custid, SUM(saleprice) AS '주문합계'
# 	FROM Orders
# 	GROUP BY custid;

# SELECT * FROM vOrder;

# DROP VIEW vw_Orders;