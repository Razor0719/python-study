import pymysql

# 打开数据库连接
db = pymysql.connect('127.0.0.1', 'test', 'secret', 'test')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()
