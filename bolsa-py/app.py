import os
import pymysql.cursors
# baseName = os.environ['MYSQL_DATABASE']
# host=os.environ['MYSQL_HOST']
# port=int(os.environ['MYSQL_PORT'])
# user=os.environ['MYSQL_USER']
# password=os.environ['MYSQL_PASSWORD']

baseName = 'bolsa'
host='localhost'
port=3320
user='user'
password=123

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=baseName,
                             charset='utf8mb4',
                             port=port,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `tit` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()