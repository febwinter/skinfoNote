-- 4
SELECT employee_id, CONCAT(last_name,' ',first_name) AS 'Name',
			salary, ROUND(salary * 1.123,0) AS 'Increased Salary'
FROM employees
WHERE department_id LIKE 60;