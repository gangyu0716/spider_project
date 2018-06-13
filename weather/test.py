import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='gy000940',
                             charset='utf8',
                             db='scrapyDB',cursorclass=pymysql.cursors.DictCursor
                             )
def mysql_insert:

    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO weather(date,week,temperature,weather,wind,img)
                    VALUES (%s, %s,%s,%s,%s,%s)"""
            cursor.execute(
                sql, ('撒', '22', '33', '44', '55', '66'))

        connection.commit()

    finally:
        connection.close()
def mysql_select:

    try:
        with connection.cursor() as cursor:
            sql = """select * from weather"""
            cursor.execute(sql)
            data = cursor.fetchall()
            print (type(data))
            print (data[10])
        connection.commit()
    finally:
        connection.close()