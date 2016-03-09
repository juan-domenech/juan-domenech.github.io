# Python and MySQL
# http://stackoverflow.com/a/34503728
#  *** No need to install binaries. Python has native modules to use as MySQL interface ***

# Using demo database http://dev.mysql.com/doc/employee/en/sakila-structure.html

# Install:
# pip install pymysql
import pymysql
import pymysql.cursors

DEBUG = False

# Connect to the database (the 'test_user' has to be created previously and have full access to its schema, in this case 'employees')
# Hint: MySQLWorkbench -> Server -> Users&Privileges -> Add Account
connection = pymysql.connect(host='localhost',
                             user='test_user',
                             password='test_password',
                             db='employees',
                             #charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

def debug(message):
	print "DEBUG:",message

def get_employee_by_employee_number(emp_no):
	sql = "SELECT * FROM employees WHERE emp_no = '"+str(emp_no)+"';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_title_by_employee_number(emp_no):
	sql = "SELECT title FROM titles WHERE emp_no = '"+str(emp_no)+"' and to_date = '9999-01-01';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_department_number_by_employee_number(emp_no):
	sql = "SELECT dept_no FROM dept_emp WHERE emp_no = '"+str(emp_no)+"' and to_date = '9999-01-01';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_department_name_by_employee_number(emp_no):
	sql = "SELECT dept_name FROM departments WHERE dept_no = '"+ get_department_number_by_employee_number(emp_no)['dept_no'] +"' ;"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_salary_by_employee_number(emp_no):
	sql = "SELECT salary FROM salaries WHERE emp_no = '"+str(emp_no)+"' and to_date = '9999-01-01';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_department_manger_number_by_department_number(dept_no):
	sql = "SELECT emp_no FROM dept_manager WHERE dept_no = '"+str(dept_no)+"' and to_date = '9999-01-01';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def get_deparment_manager_name_by_employee_number(emp_no):
	sql = "SELECT first_name,last_name FROM employees WHERE emp_no = '"+ str ( get_department_manger_number_by_department_number( get_department_number_by_employee_number(emp_no)['dept_no'] )['emp_no'] ) +"';"
	cursor.execute(sql)
	result = cursor.fetchall()[0]
	if DEBUG:
		debug(sql)
		debug(result)
	return result

def search_employee_by_name(string):
	sql ="SELECT emp_no, first_name, last_name FROM employees WHERE first_name LIKE '%"+string+"%' or last_name LIKE '%"+string+"%';"
	cursor.execute(sql)
	result = cursor.fetchall()
	if DEBUG:
		debug(sql)
		debug(result)
	return result


# Example: Get employee details by employee number
employee_number = 100001

result = get_employee_by_employee_number(employee_number)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Employee not found"
else:
	print "Employee Number:",result['emp_no']
	print "First Name:",result['first_name']
	print "Last Name:",result['last_name']
	print "Gender:",result['gender']
	print "Birth Date:",result['birth_date']
	print "Hire Date:",result['hire_date']

result = get_title_by_employee_number(employee_number)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Title not found"
elif len(result) > 1:
	print "ERROR: Too many matches"
else:
	print "Employee Title:",result['title']


result = get_salary_by_employee_number(employee_number)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Salary not found"
elif len(result) > 1:
	print "ERROR: Too many matches"
else:
	print "Salary: ",result['salary']


result = get_department_name_by_employee_number(employee_number)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Department not found"
elif len(result) > 1:
	print "ERROR: Too many matches"
else:
	print "Department: ",result['dept_name']


result = get_deparment_manager_name_by_employee_number(employee_number)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Manager not found"
elif len(result) > 2:
	print "ERROR: Too many matches"
else:
	print "Manager: ",result['first_name'],result['last_name']



# Example: Employee by free text search
string_to_search = 'gianluca'
print
print "Search: ", string_to_search
result = search_employee_by_name(string_to_search)

if DEBUG:
	debug(result)

if not result:
	print "ERROR: Name not found"
elif len(result) > 300:
	print "ERROR: Too many matches. Narrow your seach"
else:
	print len(result),"employees found."
	for item in range(0,len(result)):
		print result[item]['emp_no'], result[item]['first_name'], result[item]['last_name']

