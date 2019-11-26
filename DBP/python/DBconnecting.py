import pymysql.cursors

#conn = pymysql.connect(host='192.168.56.103', port=4567 ,user='project_user',password='Sjrnfl1!2!',db='madang')
conn = pymysql.connect(host='localhost', port=3306, user='root', password ='sjrnfl12', db='ATMProject')
cur = conn.cursor()
sql = 'Show tables'
cur.execute(sql)
res = cur.fetchall()
print(res)