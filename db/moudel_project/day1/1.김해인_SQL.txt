-- 1
SELECT CONCAT(first_name, ' ', last_name) AS 'Name',
			job_id AS 'Job', salary AS 'Salary', (12 * salary + 100) AS 'Increased Ann_Salary',
 			12 * (salary + 100) AS 'Increased Salary'
FROM employees;

-- 2
SELECT CONCAT(last_name,': 1 Year Salary = $', (salary * 12)) AS '1 Year Salary' 
FROM employees;

-- 3
SELECT CONCAT(first_name,' ', LAST_name) AS 'Name', 
			salary,
			job_id, 
			commission_pct
FROM employees
ORDER BY salary DESC, commission_pct DESC;

-- 4
SELECT employee_id, CONCAT(last_name,' ',first_name) AS 'Name',
			salary, ROUND(salary * 1.123,0) AS 'Increased Salary'
FROM employees
WHERE department_id LIKE 60;

-- 5
SELECT CONCAT(UPPER(SUBSTR(first_name,1,1)),SUBSTR(first_name,2,CHAR_LENGTH(first_name)-1), ' ', 
		UPPER(SUBSTR(last_name,1,1)),SUBSTR(last_name,2,CHAR_LENGTH(last_name)-1), ' is a ',UPPER(job_id))
FROM employees
WHERE last_name LIKE '%s'
-- 이름, 성 첫글자 대문자화 추가하기

-- 6
SELECT CONCAT(first_name, ' ', last_name) AS 'Name',
			salary, 
			IF(commission_pct IS NULL, salary * 12, salary * 12 * (1 + commission_pct)) AS 'Ann_salary', 
			IF(commission_pct IS NULL,'Salary only','Salary + Commission') AS '수당여부'
FROM employees
ORDER BY 'Ann_salary' DESC;

-- 7
SELECT department_id, 
		CONCAT('$',FORMAT(SUM(salary),0)) AS '급여합', 
		CONCAT('$',FORMAT(AVG(salary),0)) AS '평균 급여', 
		CONCAT('$',FORMAT(MAX(salary),0)) AS '최고 급여', 
		CONCAT('$',FORMAT(MIN(salary),0)) AS '최저 급여'
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id
ORDER BY department_id ASC

-- 8
SELECT job_id, AVG(salary) AS 'Avg Salary'
FROM employees
WHERE job_id NOT LIKE '%CLERK%'
GROUP BY job_id
HAVING AVG(salary) > 10000
ORDER BY 'Avg Salary' DESC

-- 9
SELECT 'Han-Bit',
			CONCAT(first_name,' ',last_name) AS 'Name',
			job_id,
			departments.department_name,
			locations.city
FROM employees, departments, locations
WHERE employees.department_id = departments.department_id
		AND departments.location_id = locations.location_id
		and departments.location_id = (
			SELECT location_id
			FROM locations
			WHERE city = 'Oxford'
		);

-- 10

SELECT d.department_name, COUNT(*) AS '사원수'
FROM employees e, departments d
WHERE e.department_id = d.department_id
GROUP BY d.department_name
HAVING COUNT(*) >= 5
ORDER BY '사원수' DESC;

-- 11

SELECT CONCAT(e.first_name,' ',e.last_name) AS 'Name',
			e.job_id,
			d.department_name,
			e.hire_date,
			e.salary,
			jg.grade_level
			
FROM employees e, departments d, job_grades jg
WHERE e.department_id = d.department_id AND
		e.salary BETWEEN jg.lowest_sal AND jg.highest_sal;

-- 12

SELECT CONCAT(e.first_name,' ',e.last_name) AS 'Name',
			e.job_id,
			e.salary
FROM employees e
WHERE e.salary > (SELECT salary FROM employees
							WHERE last_name LIKE 'Tucker');

-- 13

SELECT CONCAT(a.first_name,' ',a.last_name) AS 'Name',
			a.job_id,
			a.salary,
			a.hire_date
FROM employees a
WHERE a.salary LIKE ( SELECT MIN(b.salary) FROM employees b
								WHERE a.job_id = b.job_id);


-- 14


SELECT CONCAT(e.first_name,' ',e.last_name) AS 'Name',
			e.salary,
			e.department_id,
			e.job_id
FROM employees e
WHERE e.salary > (SELECT AVG(et.salary) FROM employees et 
						WHERE e.department_id = et.department_id 
						);

-- 15

SELECT e.employee_id, CONCAT(e.first_name,' ',e.last_name) AS 'Name', e.job_id, e.hire_date
FROM employees e, departments d, locations l
WHERE e.department_id = d.department_id 
		AND d.location_id = l.location_id
		AND l.city LIKE 'O%';

-- 16

SELECT CONCAT(e.first_name,' ',e.last_name) AS 'Name',
			e.job_id,
			e.salary,
			e.department_id,
			(SELECT AVG(et.salary)
				FROM employees et
				WHERE e.department_id = et.department_id) AS 'Department Avg Salary'
FROM employees e;

-- 17

SELECT e.employee_id, e.job_id
FROM employees e, job_history jh
WHERE e.employee_id = jh.employee_id
		AND jh.job_id = e.job_id;

-- 18

SELECT jh.start_date, jh.end_date
FROM employees e, job_history jh
WHERE e.employee_id = jh.employee_id
		AND jh.job_id = e.job_id
		AND e.employee_id LIKE 176;

-- 19

SELECT e.department_id, SUM(e.salary) AS 'Department salary',
		case
			when SUM(e.salary)  > 100000
			then 'Excellent'
			when SUM(e.salary) > 50000
			then 'Good'
			when SUM(e.salary) > 10000
			then 'Medium'
			when SUM(e.salary) <= 10000
			then 'Well'
		END AS 'Salary Grade'
FROM employees e, departments d
WHERE e.department_id = d.department_id
GROUP BY d.department_id;

-- 20

SELECT CONCAT(first_name,' ',last_name) AS 'Name', e.job_id, 
		case 
			when e.job_id LIKE '%MGR%' 
					AND e.hire_date < STR_TO_DATE('2015-01-01','%Y-%m-%d')
			then FORMAT(e.salary * 1.15,0)
			when e.job_id LIKE '%MAN%' 
					AND e.hire_date < STR_TO_DATE('2015-01-01','%Y-%m-%d')
			then FORMAT(e.salary * 1.20,0)
			when e.job_id LIKE '%MGR%' 
					AND e.hire_date > STR_TO_DATE('2015-01-01','%Y-%m-%d')
			then FORMAT(e.salary * 1.25,0)
		END AS 'Increased Salary'
FROM employees e
WHERE e.job_id LIKE '%MGR%' OR e.job_id LIKE	'%MAN%';









