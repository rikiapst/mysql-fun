import pymysql
 
# 1. Install pymysql to local directory
# pip install -t $PWD pymysql
 
# 2. (If Using Lambda) Write your code, then zip it all up 
# a) Mac/Linux --> zip -r9 ${PWD}/function.zip 
# b) Windows --> Via Windows Explorer
 
# Lambda Permissions:
# AWSLambdaVPCAccessExecutionRole
 
#Configuration Values
endpoint = 'database-1.co1vivjyehts.us-east-2.rds.amazonaws.com'
username = 'admin'
password = 'databasetest'
database_name = 'rdstest'

#Connection
connection = pymysql.connect(host=endpoint, user=username,
	password=password, db=database_name)
 
def lambda_handler():
	cursor = connection.cursor()
	cursor.execute('SELECT * from Conversation')
	rows = cursor.fetchall()
 
	for row in rows:
		print("{0} {1} {2} {3} {4}".format(row[0], row[1], row[2], row[3], row[4]))

lambda_handler()