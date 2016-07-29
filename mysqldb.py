#coding: utf-8
import MySQLdb.cursors
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='test', charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
cursor = conn.cursor()
sql = 'select address from result_ports'
cursor.execute(sql)
data = cursor.fetchone()

print data
print type(data)
conn.close()
