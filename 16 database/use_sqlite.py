import sqlite3

connect = sqlite3.connect('test.db')
cursor = connect.cursor()
cursor.execute('drop table if exists user')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
connect.close()