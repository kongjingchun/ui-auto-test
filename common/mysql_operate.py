# encoding: utf-8
# @File  : mysql_operate.py
# @Author: 孔敬淳
# @Date  : 2025/12/23/11:49
# @Desc  : MySQL数据库操作类，提供数据库连接、查询、增删改等功能
from common.yaml_config import GetConf
import pymysql


class MysqlOperate:
    """MySQL数据库操作类"""

    def __init__(self):
        """初始化数据库配置信息"""
        # 从配置文件中读取MySQL配置
        mysql_config = GetConf().get_mysql_config()
        self.host = mysql_config["host"]
        self.port = mysql_config["port"]
        self.user = mysql_config["user"]
        self.password = mysql_config["password"]
        self.db = mysql_config["db"]
        self.conn = None  # 数据库连接对象
        self.cur = None  # 游标对象

    def __conn_db(self):
        """连接数据库
        
        Returns:
            bool: 连接成功返回True，失败返回False
        """
        try:
            # 建立MySQL数据库连接
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset="utf8")
        except Exception as e:
            print(f"数据库连接失败: {e}")
            return False
        # 创建游标对象
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        """关闭数据库连接
        
        Returns:
            bool: 关闭成功返回True
        """
        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭连接
        return True

    def __commit(self):
        """提交事务
        
        Returns:
            bool: 提交成功返回True
        """
        self.conn.commit()
        return True

    def query(self, sql):
        """查询数据
        
        Args:
            sql: SQL查询语句
            
        Returns:
            tuple: 查询结果，如果没有数据返回None
        """
        self.__conn_db()  # 连接数据库
        self.cur.execute(sql)  # 执行SQL语句
        query_data = self.cur.fetchall()  # 获取所有查询结果
        if query_data == ():
            query_data = None
            print("没有获取到数据")
        self.__close_conn()  # 关闭连接
        return query_data

    def insert_update_delete(self, sql):
        """执行插入、更新或删除操作
        
        执行INSERT、UPDATE或DELETE等数据修改操作，会自动提交事务
        
        Args:
            sql: SQL语句（INSERT、UPDATE或DELETE）
            
        Example:
            insert_update_delete("INSERT INTO user (name, age) VALUES ('张三', 25)")
            insert_update_delete("UPDATE user SET age = 26 WHERE name = '张三'")
            insert_update_delete("DELETE FROM user WHERE name = '张三'")
        """
        self.__conn_db()  # 连接数据库
        self.cur.execute(sql)  # 执行SQL语句
        self.__commit()  # 提交事务
        self.__close_conn()  # 关闭连接



if __name__ == '__main__':
    result = MysqlOperate().query("select * from user;")
    print(result)
    print(result[0][1])

