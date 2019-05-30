import sqlite3

DB_FILES = 'db/database.db'


# 创建数据库
def create_tables():
    f_name = 'db/store-schema.sql'
    with open(f_name, 'r', encoding='utf-8') as f:
        sql = f.read()
        # 创建数据库连接
        conn = sqlite3.connect(DB_FILES)
        try:
            # 执行多条不同sql语句
            conn.executescript(sql)
            print('数据库初始化成功')
        except Exception as e:
            print(e)
            print('数据库初始化失败')
        finally:
            conn.close()


# 数据库商品表的插入
def load_data():
    f_name = 'db/store-dataload.sql'
    with open(f_name, 'r', encoding='utf-8') as f:
        sql = f.read()
        # 创建数据库连接
        conn = sqlite3.connect(DB_FILES)
        try:
            # 执行多条不同sql语句
            conn.executescript(sql)
            print('数据插入成功')
        except Exception as e:
            print(e)
            print('数据库插入失败')
        finally:
            conn.close()
