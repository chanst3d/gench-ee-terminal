import mysql.connector
from mysql.connector import Error

# 数据库连接配置
config = {
    'host': 'sh-cdb-c4iyam20.sql.tencentcdb.com',
    'port': 37297,
    'user': 'root',
    'password': 'Cwq20040211@',
    'database': 'gench-ee',  # 替换为您的数据库名称
    'raise_on_warnings': True
}

try:
    # 创建数据库连接
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("成功连接到MySQL服务器，版本为：", db_info)
        
except Error as e:
    print("连接错误：", e)