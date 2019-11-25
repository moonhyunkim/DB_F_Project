import pymysql.cursors

conn = pymysql.connect(host='192.168.56.103', port=4567 ,user='project_user',password='Sjrnfl1!2!',db='madang')
cur = conn.cursor()
sql = 'select * from Book'
cur.execute(sql)
res = cur.fetchall()
print(res)