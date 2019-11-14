from sqlml import Sql                   
from tkinter import *
def denglu(zhanghao,mima):

    sql='select 用户名 from 用户表'                                #sql命令
    zh=Sql.sql1(sql)                                            


    for x in zh:
        if zhanghao==x[0]:            
            sql="select 密码 from 用户表 where 用户名='"+x[0]+"'"
            mm=Sql.sql1(sql)
            print(mm)
            if mm[0][0]==mima:
                print('登陆成功!!!!!!!!!!!!!')
                return 1            
                ########################################################################
               
            else:
                xi=Tk()
                xi.geometry('450x150')
                l=Label(xi,text='密码错误')
                l.pack()
                xi.mainloop()
                return 0
    
    xi=Tk()
    xi.geometry('450x150')
    l=Label(xi,text='账号错误')
    l.pack()
    xi.mainloop()
    return 0