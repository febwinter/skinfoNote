# 1
# USE madang

# CREATE OR REPLACE VIEW highorders
# AS 
# SELECT Book.bookid, Book.bookname, Customer.name, Book.publisher, Book.price
# FROM Book, Customer, Orders
# WHERE Book.price LIKE 20000
# GROUP BY bookid;

# SELECT * 
# from highorders;

# 2
# USE madang

# CREATE OR REPLACE VIEW highorders(bookid, bookname, publisher)
# AS 
# SELECT Book.bookid, Book.bookname, Book.publisher
# FROM Book, Customer
# WHERE Book.price LIKE 20000
# GROUP BY bookid;

# SELECT * 
# FROM highorders;

# 3
# USE mydb

# SELECT CONCAT(first_name, ' ', last_name) AS name
# FROM employees
# WHERE manager_id IS NULL;

# 4
#join
# SELECT CONCAT(first_name, ' ', last_name) AS ename, department_name
# FROM employees e, departments d
# WHERE e.department_id = d.department_id;

# sub query
# SELECT CONCAT(first_name, ' ', last_name) AS ename,
# 			(SELECT department_name
# 			FROM departments d
# 			WHERE d.department_id = e.department_id) dname
# FROM employees e;

# 5

# SELECT first_name
# FROM employees, departments
# WHERE employees.department_id = departments.department_id
# AND location_id = (
# 	SELECT location_id
# 	FROM locations
# 	WHERE city LIKE 'Seattle'
 #);

# 6

# SELECT CONCAT(first_name + ' ' + last_name)
# FROM employees e JOIN department d
# 	ON e.department_id = d.department_id
# WHERE salary > (
# 	SELECT AVG(salary) FROM employees);

# 7

SELECT CONCAT(first_name + ' ' + last_name) AS 'name'
FROM employees e JOIN departments d
	ON e.department_id = d.department_id
WHERE salary > (
	SELECT AVG(salary) FROM employees
 	WHERE department_id = e.department_id);