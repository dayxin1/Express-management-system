import pymssql   #模块:sql server
class Sql:


    def sql1(self):
        #print(sql)
        serverName = '127.0.0.1'                                 #sql服务器名，这里(127.0.0.1)是本地数据库IP                                  
        userName = 'sa'                                                        #登陆用户名和密码
        passWord = '1'                                                         #建立连接并获取cursor
        conn = pymssql.connect(serverName , userName , passWord, "kd")            #连接数据库
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        cur =  conn.cursor()                                       #创建游标 提交sql语句
        cur.execute(self)                                         #提交sql命令
        fanhui=cur.fetchall()                                      #获取查询结果 在fanhui列表中以[( ,),( ,)]保存
        cur.close()                                                #关闭游标
        conn.close()
        if fanhui == []:
            fanhui = [('',),]
        return fanhui
#sql6="select 省会城市 from 省份表 where 省份='安徽'"
#shcs=Sql.sql1(sql6)                             #shcs 省会城市
#print(shcs)


    def sql2(self):
            #print(sql)
            serverName = '127.0.0.1'                                 #sql服务器名，这里(127.0.0.1)是本地数据库IP                                  
            userName = 'sa'                                                        #登陆用户名和密码
            passWord = '1'                                                         #建立连接并获取cursor
            conn = pymssql.connect(serverName , userName , passWord, "kd")            #连接数据库
            #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            cur =  conn.cursor()                                       #创建游标 提交sql语句
            cur.execute(self)                                           #提交sql命令
            conn.commit()                                               #确认执行sql命令
            cur.close()                                                #关闭游标
            conn.close()
