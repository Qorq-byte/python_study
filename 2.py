import os

import pymysql

# 1. 建立数据库连接
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password=os.environ["MYSQL_PASSWORD"],
    database="mysql"           # 先连系统库测试
)

# 2. 创建游标，执行SQL
cursor = conn.cursor()
cursor.execute("SHOW DATABASES;")
result = cursor.fetchone()
print("MySQL 版本:", result)

# 3. 关闭资源
cursor.close()
conn.close()
