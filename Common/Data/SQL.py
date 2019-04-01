import pymysql
class U_P_SQL():
    def usename_pasword(self,m,n):
        connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db="zentao",charset='utf8')
        # 使用游标操作
        cursor = connection.cursor()
        # 获取表的全部数据fetchall
        q = cursor.execute('select * from user')
        # 使用fetchall查询全部数据
        user_pw = cursor.fetchall()[m]
        username_password=user_pw[n]
        return username_password

