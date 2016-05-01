#!/usr/bin/python

import MySQLdb
import math

# Open database connection
db = MySQLdb.connect("localhost","root","zing","fov" )


# prepare a cursor object using cursor() method
cursor = db.cursor()
sum=0
num =0
elements1 = []
elements2 = []
sql = "select health.country_code , health.2010 from health"
try:
	cursor.execute(sql)
	#db.commit()
	rows = cursor.fetchall()
	print('Total Row(s):', cursor.rowcount)
	for row in rows:
		elements1.append(row[0])
		elements2.append(row[1])
		num = row[1]
		sum = sum + num*num
except:
	print "Error"
	#db.rollback()
# for i in elements:
# 	sum = sum + i
sum = math.sqrt( sum )
print(sum)

# cursor.execute("DROP TABLE IF EXISTS healthRev")
sql = "CREATE TABLE healthRev (\
         country_code  varchar(63) NOT NULL,\
         `2010`  double ,cluster varchar(10))"
#cursor.execute(sql)
count = 0
while (count < 248):
	sql2 = "INSERT INTO healthRev (country_code, `2010`) VALUES ('%s','%lf')" %(elements1[count],(elements2[count]/sum)*100)
	try:
		
		cursor.execute(sql2)
		db.commit()
	except:
		print "Error"
		db.rollback()
	count = count + 1
country = []
year = []
sql = "select country_code, `2010` from healthRev"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
	country.append(row[0])
	year.append(row[1])
for i in country:
	print i
for i in year:
	print i
count=0
# while (count<248):	
# 	if (year[count]<=2):
# 		#cursor.execute("UPDATE healthRev SET `2010` = 1 where country_code = '%s'" %(country[count]))
# 		year[count] = 1;
# 	count = count+1;
# count=0
# while(count<248):
# 	print year[count]
# 	count = count+1

# disconnect from server
db.close()
