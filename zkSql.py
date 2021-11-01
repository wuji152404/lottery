import pymysql


class ZkSql():
    def __init__(self,host='124.71.144.16',port=13779,user='testgroup',passwd="ffgUp9zq9kKZi2z",dbName='test_zy2020'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.dbName=dbName

    def connet(self):
        config = {'host': '124.71.144.16', 'port': 13779, 'user': 'testgroup', 'passwd': 'ffgUp9zq9kKZi2z',
                  'db': 'test_zy2020'}
        self.db = pymysql.connect(**config)
        # self.db=pymysql.connect(self.host,self.port,self.user,self.passwd,self.dbName)
        self.cursor=self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res=None
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            self.close()
        except:
            print('查询失败')
        return res

    def get_all(self,sql):
        res=None
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            self.close()
        except:
            print('查询失败')
        return res
    def insert(self,sql):
        return self.__edit(sql)
    def update(self,sql):
        return self.__edit(sql)
    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count=0
        try:
            self.connet()
            count=self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('事物提交失败')
            self.db.rollback()
        return count

if __name__ == '__main__':
    a=ZkSql('124.71.144.16',13779,'testgroup','ecc01ea551efe7R','test_zy2020')
    # #res=ZkSql('192.168.1.1','root','','zhuke').get_all('select * from bandcard')
    # a.connet()
    sql="desc lot_level_product"

    #插入数据
    a.insert()