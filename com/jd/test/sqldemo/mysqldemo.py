import mysql.connector
conn = mysql.connector.connect(user='root', password='', database='mybatis', use_unicode=True)
cursor=conn.cursor()
cursor.execute('SELECT * from t_user WHERE user_id= %s', ('11',))
values = cursor.fetchall()
print values
cursor.close()