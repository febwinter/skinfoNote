# ------------------------------------------------------
# madang quiz
# 1
# SELECT SUM(saleprice) AS '박지성 총 구매액' from Orders WHERE custid=1;

# 2
#SELECT COUNT(*) AS '박지성 구매 횟수' FROM Orders WHERE custid=1;

#3 - 미완성  
# SELECT Orders.custid, Book.publisher
# FROM Orders, Book
# WHERE Orders.bookid = Book.bookid
# GROUP BY publisher
# HAVING COUNT(SELECT publisher FROM )


# 7
#SELECT *
#FROM Orders
#WHERE orderdata NOT BETWEEN '2014-07-04' AND '2014-07-07'

# 9
#SELECT NAME, AVG(saleprice)
#FROM Customer, Orders
#WHERE Customer.custid = Orders.custid
#GROUP BY NAME
#HAVING AVG(saleprice) > (SELECT AVG(saleprice) FROM Orders)

# 10
# SELECT NAME
# FROM Customer, Orders, Book
# WHERE Customer.custid = Orders.custid
#	AND Orders.bookid=Book.bookid
#	AND NAME NOT LIKE '박지성' AND publisher IN 
# (SELECT publisher FROM Customer, Orders, Book
# WHERE Customer.custid = Orders.custid 
#		AND Orders.bookid = Book.bookid
#		AND NAME LIKE '박지성')

# 
# SELECT NAME FROM Customer AS c1
# WHERE 2 <= (
# SELECT COUNT(publisher) FROM Customer, Orders, Book
# WHERE Customer.custid=Orders.custid
# 	AND Orders.bookid=Book.bookid
# 	AND (NAME LIKE c1.name)
# 	)

# 12
# SELECT bookname FROM Book b1
# WHERE ( (SELECT COUNT(Book.bookid)
# 				FROM Book,orders
# 				WHERE Book.bookid=Orders.bookid
# 				AND Book.bookid=b1.bookid) >=
# 				0.3 * (SELECT COUNT(*) FROM customer)
# 		);

# ---------------------------------------------------------
# mydb quiz

# 1
# SELECT manager
# FROM Department;

# 2
# SELECT NAME, address
# FROM Employee
# WHERE Employee.deptno = (
# 	SELECT deptno
# 	FROM Department
# 	WHERE Department.deptname LIKE 'IT'	
# );

# 3
# SELECT COUNT(*) AS '사원의 수' 
# FROM Employee
# WHERE deptno =  (
# 	SELECT deptno FROM Department WHERE manager='홍길동'
# );

# 4
# SELECT Employee.name ,Works.hoursworked
# FROM Employee, Works
# WHERE Employee.empno = Works.empno
# ORDER BY Works.hoursworked ASC;

# 5
# SELECT Project.projno, Project.projname, COUNT(*) AS Total
# FROM Project, Works
# WHERE Project.projno = Works.projno
# GROUP BY Works.projno
# HAVING Total >= 2;

# 6
# SELECT Employee.name
# FROM Employee, Department
# WHERE Employee.deptno = Department.deptno 
# 		AND Department.deptname = (
# 			SELECT deptname FROM Employee, Department
# 			WHERE Employee.deptno = Department.deptno 
# 			GROUP BY Department.deptname
# 			HAVING COUNT(NAME) >= 3
# 		);