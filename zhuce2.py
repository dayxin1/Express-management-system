from sqlml import Sql                   
from tkinter import *

def zhuce():                                            #注册页面
    def pd():                                             # 只供   zhuce()  调用,判断输入用户名 是否合法
        e11=e1.get()                                       #############
        e21=e2.get()                                       #e11-e31获取输入框信息 e1用户名 e2密码 e3 手机号
        e31=e3.get()                                        #########
        sql='select 用户名 from 用户表'                     #调用自定义sql连接中的查询模块,并返回查询结果
        zh=Sql.sql1(sql)                                                     #将所有用户名存进 zh
        if e11=='':
            xi=Tk()                                             #新建窗口
            xi.geometry('450x150')
            l=Label(xi,text='用户名为空',font=('Arial',15))                      #遍历判断用户名重复,并弹窗提示
            l.pack()
            xi.mainloop()
            return 0


        for x in zh:                                           #********************

            if x[0]==e11:
                xi=Tk()                                             #新建窗口
                xi.geometry('450x150')
                l=Label(xi,text='用户名重复',font=('Arial',15))                      #遍历判断用户名重复,并弹窗提示
                l.pack()
                xi.mainloop()
                return 0                                           # 用户名重复便跳出
        if e21=='':                                                #**********8
            xi=Tk()
            xi.geometry('450x150')
            l=Label(xi,text='密码为空',font=('Arial',15))                             #密码不能为空
            l.pack()
            xi.mainloop()
            return 0
        
        sql="insert into 用户表(用户名,密码,电话) values('%s','%s','%s')"%(e11,e21,e31)
        Sql.sql2(sql)                                               #将合法用户名密码添加进数据库

        xi=Tk()
        l=Label(xi,text='注册成功!\n用户名:%s\n密码:%s\n电话:%s\n用户权限: 普通用户'%(e11,e21,e31))
        l.pack()
        xi.mainloop()

        return 1

    zhuce1=Tk()
    zhuce1.title('注册')
    e1=Entry(zhuce1)
    e2=Entry(zhuce1)
    e3=Entry(zhuce1)
    l1=Label(zhuce1,text='用户名')
    l2=Label(zhuce1,text='密码')
    l3=Label(zhuce1,text='手机号')
    b=Button(zhuce1,text='确定',command=pd)
    e1.place(x = 50,y = 10)
    e2.place(x = 50,y = 50)
    e3.place(x = 50,y = 90)
    l1.place(x = 10,y = 10)
    l2.place(x = 10,y = 50)
    l3.place(x = 10,y = 90)
    b.place(x = 70,y = 130)
    zhuce1.mainloop()
    
