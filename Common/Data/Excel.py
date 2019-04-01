import xlrd
class U_P_Excel():
    def User(self,m,n):
        self.data = xlrd.open_workbook('D:\\禅道\\Common\\Data\\用户名密码.xls')
        sheet = self.data.sheets()[0]
        row_value = sheet.row_values(m)
        user = row_value[n]
        return user

    def Int_Password(self,m,n):#从Excel表中去取出的数字数为字符串，所以密码要单独写个方法    123456    123456.0
        self.data = xlrd.open_workbook('D:\\禅道\\Common\\Data\\用户名密码.xls')
        sheet = self.data.sheets()[0]
        # 以行查询数据
        row_value = sheet.row_values(m)
        password = int(row_value[n])
        return password

    def zero_password(self,m,n):
        self.data = xlrd.open_workbook('D:\\禅道\\Common\\Data\\用户名密码.xls')
        sheet = self.data.sheets()[0]
        # 以行查询数据
        row_value = sheet.row_values(m)
        password = row_value[n]
        return password









