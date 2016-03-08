# Python and MySQL
# http://stackoverflow.com/a/34503728
#  *** No need to install binaries. Python has native modules to use as MySQL interface ***

# Just for this demo (let's create some MD5 hashes)
import hashlib

# Install:
# pip install pymysql
import pymysql
import pymysql.cursors

# Connect to the database (the 'test' user has to be created previously and have full access to its schema, in this case 'test')
# Hint: MySQLWorkbench -> Server -> Users&Privileges -> Add Account
connection = pymysql.connect(host='localhost',
                             user='test_user',
                             password='test_password',
                             db='test_schema',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

# Drop table if exists
sql = "DROP TABLE IF EXISTS numbers;"
print sql
cursor.execute(sql)


# Write example
#
# Create table
sql = "CREATE TABLE `numbers` (`number` mediumint NOT NULL,`md5` varchar(32) NOT NULL,PRIMARY KEY (`number`),UNIQUE KEY `number_UNIQUE` (`number`)) ENGINE=InnoDB;"
print sql
cursor.execute(sql)

# Generate and Insert data into MySQL
for item in range(0,10000):
	sql = "INSERT INTO `numbers` VALUES ('"+str(item)+"','"+hashlib.md5( str(item) ).hexdigest()+"');"
	print sql
	cursor.execute(sql)

# Connection is not autocommit by default. So you must commit to save your changes.
connection.commit()


# Read example
#
print
print "Search for numbers ended with '999':"
sql = "SELECT number, md5 FROM numbers WHERE number LIKE '%999';"
print sql
cursor.execute(sql)
result = cursor.fetchall()
for item in range(0,len(result)):
	print item,result[item]

