from denglu2 import * 
from zhuce2 import * 
from sqlml import Sql                   
from tkinter import *
from tkinter import ttk 
from lujing import *
用户名=''
权限=''
def guanli():                                                     #管理界面 root6
    def shanchu(): #删除选中的记录
        a=v.get()
        if a != NONE:
            for x,y in lb: #选中按钮在第一列 用户
                if a==y:

                    yhm=''
                    for i in x:
                        if i!= ' ':
                            yhm+=i
                        else:
                            break
                    yhm=yhm[4:]
                    sql="DELETE FROM 用户表 WHERE 用户名 = '%s'"%(yhm)
                    Sql.sql2(sql)
                    root6.destroy()
                    guanli()
            for x,y in lb2:     #选中按钮在第二列 快递单
                if a==y:
                    kdd=x
                    kdd=kdd[5:]
                    kdd=kdd[:11]
                    sql="DELETE FROM 快递表 WHERE 快递单号 = '%s'"%(kdd)
                    Sql.sql2(sql)
                    root6.destroy()
                    guanli()

    def xiugai(): #修改
        def querenxiugai1():
            e1=e.get()
            e2=e8.get()
            print(e2)
            c=cmb1.get()
            if c=='管理员':
                c=0
            elif c=='普通用户':
                c=1
            sql="UPDATE 用户表 SET 用户类别 = %s WHERE 用户名 = '%s'"%(str(c),yhm)
            Sql.sql2(sql)

            if e1 != '':
                sql="UPDATE 用户表 SET 密码 = '%s' WHERE 用户名 = '%s'"%(e1,yhm)
                Sql.sql2(sql)
            
            if  e2 != '':
                sql="UPDATE 用户表 SET 电话 = '%s' WHERE 用户名 = '%s'"%(e2,yhm)
                Sql.sql2(sql)
            xi1.destroy()
            root6.destroy()
            guanli()
        def querenxiugai2():
            c=cmb1.get()
            i=0
            for x in k:
                i=i+1
                if x==c:
                    sql="UPDATE 快递表 SET 到达位置 = '%s' WHERE 快递单号 = '%s'"%(str(i),kdd)
                    Sql.sql2(sql)
                    break
            xi1.destroy()
            root6.destroy()
            guanli()


        a=v.get()
        if a != NONE:

            for x,y in lb:
                if a==y:
                    yhm=''
                    for i in x:
                        if i!= ' ':
                            yhm+=i
                        else:
                            break
                    yhm=yhm[4:]

                    xi1=Tk()
                    xi1.geometry('560x200')
                    l1=Label(xi1,text='用户名:%s'%(yhm),font=('Arial',20))
                    l2=Label(xi1,text='用户级别: ')
                    l3=Label(xi1,text="密码:")
                    l4=Label(xi1,text="电话:")

                    cmb1=ttk.Combobox(xi1,state='readonly')
                    cmb1['value']=('管理员','普通用户')
                    sql="select 用户类别 from 用户表 where 用户名='%s'"%(yhm)
                    jibie=Sql.sql1(sql)
                    jibie=jibie[0][0]
                    if  jibie == 0:
                        cmb1.current(0)
                    else:
                        cmb1.current(1)
                    
                    e=Entry(xi1)
                    e8=Entry(xi1)
                    b=Button(xi1,text='确认修改',command=querenxiugai1)

                    l1.place(x=10,y=10,)
                    l3.place(x=40,y=70,)
                    e.place(x=80,y=70)
                    l2.place(x=240,y=70)
                    cmb1.place(x=300,y=70)

                    l4.place(x=40,y=95)
                    e8.place(x=80,y=95)
                    b.place(x=130,y=120)
                    return 0

            for x,y in lb2:
                if a==y:
                    kdd=x
                    kdd=kdd[5:]
                    kdd=kdd[:11]

                    xi1=Tk()
                    xi1.geometry('560x200')
                    l1=Label(xi1,text='快递单号:%s'%(kdd),font=('Arial',20))
                    l2=Label(xi1,text='已到达城市: ')
                    cmb1=ttk.Combobox(xi1,state='readonly')
                    k=[]
                    a=''
                    sql="select 备注,到达位置 from 快递表 where 快递单号='%s'"%(kdd)
                    b=Sql.sql1(sql)
                    ddwz=b[0][1]
                    b=b[0][0]
                    pp=0
                    for x in b:
                        if x !='-':
                            a=a+x
                            if x == '市' or x == '区' or (x=='州' and b[pp-1]=='治'):
                                k=k+[a]
                                a=''
                        pp+=1
                    cmb1['value']=k
                    cmb1.current(int(ddwz)-1)
                    l1.place(x=10,y=10,)
                    l2.place(x=210,y=70)
                    cmb1.place(x=300,y=70)
                    b=Button(xi1,text='确认修改',command=querenxiugai2)
                    b.place(x=130,y=120)


    def fanhui3():
        root6.destroy()
        zhujiemian()
    root6 = Frame(root,width=960,height=540)
    root6.pack()
    b=Button(root6,text='返回主界面',font=('Arial',20),command=fanhui3)
    b.place(x=760,y=490) 
    
    b12=Button(root6,text='修改',font=('Arial',20),command=xiugai)
    b13=Button(root6,text='删除',font=('Arial',20),command=shanchu)

    b12.place(x=100,y=490)
    b13.place(x=200,y=490)

    sql="select *  from 用户表"
    yh=Sql.sql1(sql)
    i=0
    lb=[]
    for x in yh:
        lb=lb+[('用户名:'+yh[i][0]+'   电话号码:'+yh[i][2]+'    权限: '+str(yh[i][3]),i+1),]
        i+=1



    sql="select 快递单号,备注,到达位置  from 快递表"
    kd=Sql.sql1(sql)
    j=0
    lb2=[]

    for y in kd:
        lb2=lb2+[('快递单号:'+kd[j][0]+"    路径:"+kd[j][1]+'    到达第%s个城市'%(kd[j][2][0:2]) , i+1           ),]
        i+=1
        j+=1
    v = IntVar()
        
    y1=1
    for a , num in lb:
        b8 = Radiobutton(root6, text=a, variable=v, value=num )
        b8.place(relx=0,y=y1)#,x=0,y=y1)
        y1+=19
    y1=1
    for a,num in lb2:
        b9 = Radiobutton(root6, text=a, variable=v, value=num )
        b9.place(relx=0.3,y=y1)#,y=y1)
        y1+=19
   
def chaxun():                                               #查询快递单号 root5
    def fanhui2():
        root5.destroy()
        zhujiemian()
    def chaxun1():
        e1=e.get()
        if len(e1) != 11: #输入位数不为11位
            return 0
        else:
            sql="select 备注,到达位置 from 快递表 where 快递单号='%s'"%(e1)
            k=Sql.sql1(sql)
            if k[0][0]=='':#数据库没有该单号

                t.delete(1.0, END)
                t.insert(1.0, "%s的查询结果为空"%(e1))
                return 0
            else :
                b=k[0][0]#所有路径
                w=int(k[0][1])#到达位置
                k=[]    #将字符串转为列表 存进该变量
                a=''    #存储一个市的临时变量
                pp=0

                for x in b: #将字符串转为列表
                    if x !='-':
                        a=a+x
                        if x == '市' or x == '区':
                            k=k+[a]
                            a=''
                        if x=='州' and b[pp-1]=='治':
                            k=k+[a]
                            a=''
                    pp+=1
             
                i=0
                if w==1:    
                    a=a+'\n您的快递已从 %s中转站出发,发往 %s中转站\n'%(k[i],k[i+1])
                    a=a+'\n您的快递即将到达 %s中转站\n'%(k[i+1])
                else:               
                    while 1:
                        if i+1 >= w:
                            break
                        a=a+'\n您的快递已从 %s中转站出发,发往 %s中转站\n'%(k[i],k[i+1])
                        a=a+'\n您的快递已到达 %s中转站\n'%(k[i+1])
                        i+=1

                    if len(k)!=w:
                        a=a+'\n您的快递已从 %s中转站出发,发往 %s中转站\n'%(k[i],k[i+1])
                        a=a+'\n您的快递即将到达 %s中转站\n'%(k[i+1])
                    


                

                t.delete(1.0, END)
                t.insert(END, "%s的查询结果为\n路径:\n%s\n%s"%(e1,b,a)) 



    root5 = Frame(root,width=960,height=540)
    root5.pack()
    e=Entry(root5)
    b1=Button(root5,text='返回主界面',font=('Arial',20),command=fanhui2)
    b1.place(x=760,y=470) 
    b2=Button(root5,text='查询',command=chaxun1)
    t=Text(root5)
    e.place(x=200,y=40)
    b2.place(x=350,y=35)
    t.place(x=10,y=70)

def yijianchaxun():                                         #一键查询           root4
    def fanhui1():
        root4.destroy()
        zhujiemian()
    def fuzhi():
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        i = v.get()
        j = kk[i-1][0]
        j =j[0:11]
        r.clipboard_append('%s'%(j))
        r.update() 
        r.destroy()

    root4 =Frame(root,width=960,height=540)
    root4.pack()
    b1=Button(root4,text='返回主界面',font=('Arial',20),command=fanhui1)    
    b1.place(x=760,y=470)    
    
    sql="select 电话 from 用户表 where 用户名='%s'"%(用户名)    #查询用户名的电话
    k=Sql.sql1(sql)
    k=k[0][0]

    
    sql="select 快递单号 from 快递表 where 收件人手机号码='%s' or 寄件人手机号码='%s'"%(k,k)    #查询寄件人或者收件人电话与用户电话其\一致
    k=Sql.sql1(sql)
    if k[0][0]== '':      #  没有 提示没有快递
        l=Label(root4,text="您没有快递",font=('Arial',20))
        l.place(y=60,x=50)

    else:           #建立选择框.显示单号
        a=1
        k1=[]
        for x in k:
            sql="select 寄出市,收件市 from 快递表 where 快递单号='%s'"%(x[0])
            kk=Sql.sql1(sql)
            k1+=kk

        kk=[]
        x=0
        
        while 1:
            k2=[(k[x][0]+' '+k1[x][0]+'-'+k1[x][1],x+1,),]
            kk+=k2
            x+=1
            if x >= len(k):
                break


        v = IntVar()    #v为唯一选择框编号
        
        y1=10
        for girl,num in kk:
            b = Radiobutton(root4, text=girl, variable=v, value=num )
            b.place(x=70,y=y1)
            y1+=30
        b2=Button(root4,text="选择后点我\n把快递单号复制进剪辑板",command=fuzhi)
        b2.place(x=760,y=370)

def youjijiemian():                                         #   邮寄界面           ROOT3
    def fanhui():                #返回上一层 返回主界面
        root3.destroy()         
        zhujiemian()                                   
    def gengxin(event):          #将市选择框 与 省选择框联动
        sf=cmb1.get()               #省1选择框的输入
        sf3=cmb2.get()                 #市1选择框的输入
        sql="select 省编 from 省份表 where 省份='%s'"%(sf)
        sf=Sql.sql1(sql)
        sf=sf[0][0]                        #查询省1省编
        sql="select 市名 from 市表 where 省编='%s'"%(sf)
        sf=Sql.sql1(sql)                #查询省1 名下所有市
        sf2=()                            #用于保存省1   名下所有市
        for x in sf:
            sf2+=x[0],                  #将 [(1,),(2,),] 转化为[1,2,]
        a=0 #用于保存更新前 选中了第几个市
        for x in sf:    #遍历 名下所有的市 
            if x[0]==sf3 or sf3=='': #如果第a个市为选择的市 或者 没有选择市
                break
            else:
                a+=1
        if a >= len(sf):    #如果 a 比 市的个数多       也就是 省有变动 ,原来的市不属于变动后的省 上面for循环没有匹配成功 将a=0,默认选择更新后的第一个市
            a=0             
        print(sf,a)

        cmb2['value']=sf2#更新市选择框
        cmb2.current(a)#默认选择第a个市.意义在于如果省 市没有变动,这次更新就不改变任何东西 省有变动 默认选择第一个

        sf=cmb3.get()
        sf3=cmb4.get()
        sql="select 省编 from 省份表 where 省份='%s'"%(sf)
        sf=Sql.sql1(sql)
        sf=sf[0][0]
        sql="select 市名 from 市表 where 省编='%s'"%(sf)
        sf=Sql.sql1(sql)
        sf2=()
        for x in sf:

            sf2+=x[0],
        a=0
        for x in sf:
            if x[0]==sf3 or sf3=='':
                break
            else:
                a+=1
        if a >= len(sf):
            a=0
        print(sf,a)

        cmb4['value']=sf2
        cmb4.current(a)
    def youji():               #判断输入信息 询问是否确认邮寄   进入下级确认邮寄
        def querenjijian():        # 确认邮寄快递后 生成快递单号,并提交到数据库

            xi.destroy()            #快递单号
            kuaididanhao=''         
            sql="select 市编 from 市表 where 市名='%s'"%(jshi)
            k1=Sql.sql1(sql)
            kuaididanhao+=k1[0][0]  #寄出市市编为快递单号前4位


            sql="select 市编 from 市表 where 市名='%s'"%(sshi)
            k1=Sql.sql1(sql)
            kuaididanhao+=k1[0][0]#收件市 市编为快递单号5-8位




            sql="select 快递单号 from 快递表 "
            k1=Sql.sql1(sql)
            k1=k1[-1][0]    #查询数据库中最后一个快递单号
            
            if k1 == '':    #如果数据库中没有快递单
                k1 ='100'   #快递单最后3为为100
            else:               #有快递单号 新快递单号后3位为上一个快递单号后3位+1
                k1=k1[8:]
                print(1,k1)
                k1=int(k1)+1
                print(2,k1)
                k1=str(k1)
            kuaididanhao+=k1    #添加快递单号最后3位

            beizhu=''# 将路径城市多个变量

            if lujing2[0] == '0':#lujing2存储了省-省之间的路径 为0则为同省快递

                if jshi != sshi:    #寄出城市不为收件城市
                    beizhu=jshi+'-'
                    sql="select 省会城市 from 省份表 where 省份='%s'"%(jsheng)
                    k1=Sql.sql1(sql)
                    k1=k1[0][0]
                    if jshi != k1 and sshi != k1:
                        beizhu=beizhu+k1+'-'+sshi   #收件城市不为省会 备注=寄出城市+省会城市+收件城市
                    else :
                        beizhu=jshi+'-'+sshi    #收件城市为省会 备注=寄出城市+收件城市
                else:
                    beizhu=jshi+'-'+sshi#同市快递



            else:   #跨省快递
            
                if jshi  != lujing2[0]: #寄出城市不为省会,将寄出城市放到首位
                    beizhu=jshi+'-'
                    
                
                for x in lujing2:
                    beizhu = beizhu + x +'-'

                if sshi != lujing2[-1] :#收件城市不为省会 将收件城市放到末尾
                    beizhu = beizhu+sshi
                else:
                    beizhu = beizhu[:-1]



            sql="insert into 快递表(快递单号,寄出省,寄出市,寄出地址,寄件人姓名,寄件人手机号码,收件省,收件市,收件地址,收件人姓名,收件人手机号码,备注) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(kuaididanhao,jsheng,jshi,jdz,jxm,jdh,ssheng,sshi,sdz,sxm,sdh,beizhu)
            Sql.sql2(sql)

            xi1=Tk()
            xi1.geometry('550x650')
            l=Label(xi1,text='邮寄成功!!!\n\n 快递单号:%s \n\n由%s   %s%s%s\n寄往%s   %s%s%s\n\n途经:\n%s'%(kuaididanhao,jxm,jsheng,jshi,jdz,sxm,ssheng,sshi,sdz,beizhu),font=('Arial',15))
            l.pack()
            def guanbi():           #按钮 关闭 邮寄成功 提示框
                xi1.destroy()
            b=Button(xi1,text="关闭",command=guanbi)

            b.pack()
            xi.mainloop()
            return 0


        jsheng=cmb1.get()           #寄出省 寄出市 寄出地址 寄出姓名 寄出电话
        jshi=cmb2.get()
        jdz=e1.get()
        jxm=e11.get()
        jdh=e12.get()

        ssheng=cmb3.get()  #同上 收件省
        sshi=cmb4.get()
        sdz=e2.get()
        sxm=e21.get()
        sdh=e22.get()

        list1 = [(jsheng,jshi,jdz,jxm,jdh),(ssheng,sshi,sdz,sxm,sdh)]

        for x in list1:#双重循环 遍历每个输入框信息,如果为空则 提示
            for y in x:
                if y == '':
                    xi=Tk()
                    xi.geometry('450x150')
                    l=Label(xi,text='信息未填写完全,请重新填写!',font=('Arial',15))
                    l.pack()
                    xi.mainloop()
                    return 0       
        lujing2=lujing(list1[0][0],list1[1][0])     #调用路径函数 获取路径 并提示是否寄件
        
        if lujing2[0][0]=='0':          #返回0则为同省快递
            if list1[0][1]==list1[1][1]:    #判断是否同市快递
                xi=Tk()
                xi.geometry('450x350')
                l=Label(xi,text='同市快递\n\n由%s%s寄往\n%s%s\n\n价格:6元\n\n时间:1天\n\n确认寄件请点击\n\n取消请关闭本窗口\n\n'%(list1[0][1],list1[0][2],list1[1][1],list1[1][2]),font=('Arial',15))
                l.pack()
                b=Button(xi,text="确认寄件",command=querenjijian)
                b.pack()
                xi.mainloop()
                return 0
            else:               #同省不同市

                xi=Tk()
                xi.geometry('450x350')
                l=Label(xi,text='同省快递\n\n由%s%s寄往\n%s%s\n\n价格:8元\n\n时间:1.5天\n\n确认寄件请点击\n\n取消请关闭本窗口\n\n'%(list1[0][1],list1[0][2],list1[1][1],list1[1][2]),font=('Arial',15))
                l.pack()
                b=Button(xi,text="确认寄件",command=querenjijian)
                b.pack()
                xi.mainloop()
                return 0  
        else:       #跨省快递
            xi=Tk()
            xi.geometry('450x350')
            jiage='0'
            shijian='0'
            if len(lujing2)<=3 :
                jiage='10' 
                shijian='1.5'
            elif len(lujing2)<=6:
                jiage='12'
                shijian='3'
            else :
                jiage='15'
                shijian='3-5'

            l=Label(xi,text='全国快递\n\n由%s%s寄往\n%s%s\n\n价格:%s元\n\n时间:%s天\n\n确认寄件请点击\n\n取消请关闭本窗口\n\n'%(list1[0][0],list1[0][1],list1[1][0],list1[1][1],jiage,shijian),font=('Arial',15))
            l.pack()
            b=Button(xi,text="确认寄件",command=querenjijian)
            b.pack()
            xi.mainloop()
            return 0   
            
    root3=Frame(root,width=960,height=540)
    root3.pack()
    L1=Label(root3,text="尊敬的 %s\n 用户级别:%s"%(用户名,权限))
    L1.place(x = 800,y = 20)

    l1=Label(root3,text="寄件人地址:")
    l21=Label(root3,text="寄件人姓名:")
    l22=Label(root3,text="寄件人电话:")
    l3=Label(root3,text="收件人地址:")
    l41=Label(root3,text="收件人姓名:")
    l42=Label(root3,text="收件人电话:")
    e1=Entry(root3,width=40)
    e2=Entry(root3,width=40)
    e11=Entry(root3)
    e12=Entry(root3)
    e21=Entry(root3)
    e22=Entry(root3)
    cmb1=ttk.Combobox(root3,state='readonly')
    cmb2=ttk.Combobox(root3,state='readonly')
    cmb3=ttk.Combobox(root3,state='readonly')
    cmb4=ttk.Combobox(root3,state='readonly')
    b1=Button(root3,text='确定',font=('华康少女体',20),command=youji)
    b2=Button(root3,text='返回主界面',font=('Arial',20),command=fanhui)
    
    sql='select 省份 from 省份表'
    sf=Sql.sql1(sql)
    sf1=()
    for x in sf:
        sf1+=x[0],
    cmb1['value']=sf1
    cmb3['value']=sf1
    cmb1.current(22)
    cmb3.current(22)


    cmb1.bind("<Button-1>", gengxin)        #设定触发事件,选择省后更新市选择框
    cmb2.bind("<Button-1>", gengxin)
    cmb3.bind("<Button-1>", gengxin)
    cmb4.bind("<Button-1>", gengxin)
    b1.bind("<Button-1>", gengxin)
    
    l1.place(x = 20,y = 60)
    cmb1.place(x=90,y=60)
    cmb2.place(x=270,y=60)
    e1.place(x=450,y=60)
    l21.place(x=90,y=90)
    e11.place(x=160,y=90)
    l22.place(x=340,y=90)
    e12.place(x=420,y=90)

    l3.place(x = 20,y = 140)
    cmb3.place(x=90,y=140)
    cmb4.place(x=270,y=140)
    e2.place(x=450,y=140)
    l41.place(x=90,y=170)
    e21.place(x=160,y=170)
    l42.place(x=340,y=170)
    e22.place(x=420,y=170)
    b2.place(x=700,y=480)
    b1.place(x=420,y=300)

def zhujiemian():                                            #  主界面          ROOT2
    def tuchudenglu(): #退出登录   回到登录界面
        root2.destroy()     #销毁主界面 打开登录界面 
        denglujiemian()
    def youji1():       #进入邮寄界面 先关闭主界面容器 邮寄界面再生成新的容器
        root2.destroy()
        youjijiemian()
    def yjcx1():        #进去一键查询界面
        root2.destroy()
        yijianchaxun()
    def chaxun1():      #进去查件界面
        root2.destroy()
        chaxun()
    def guanli1():      #进入管理界面
        root2.destroy()
        guanli()
        '''
        上面都是与按钮绑定的函数
        '''



    root2=Frame(root,width=960,height=540)
    root2.pack()
    l1=Label(root2,text="尊敬的 %s\n 用户级别:%s"%(用户名,权限))
    l1.place(x = 800,y = 20)

    b1=Button(root2,text='查询快递',font=('Arial',20),command=chaxun1)
    b2=Button(root2,text='邮寄快递',font=('Arial',20),command=youji1)
    b3=Button(root2,text='一键查询\n自己的快递',font=('Arial',20),command=yjcx1)
    b4=Button(root2,text='管理\n用户\n物流信息',font=('Arial',20),command=guanli1)
    b5=Button(root2,text='退出登录',font=('Arial',20),command=tuchudenglu)
    b1.place(x = 310,y = 100)
    b2.place(x = 310,y = 180)
    if 权限=='普通用户':
        b3.place(x = 310,y = 260)
    elif 权限=='管理员':
        b4.place(x = 310,y = 260)
    b5.place(x = 700,y = 480)

def denglujiemian():                                        # 登录界面          ROOT1

    def denglu1():                   #点击 登录 按钮触发的事件
        global 用户名   #映入函数外全局变量
        global 权限
        if denglu(e1.get(),e2.get())== 1:   #将用户名 密码传递到模块 denglu2 若登陆成功则会返回 1
            用户名=e1.get()
            sql="select 用户类别 from 用户表 where 用户名='%s'"%(用户名)  #判断用户权限类别,并写去全局变量
            a=Sql.sql1(sql)
            if a[0][0] == 0:
                权限='管理员'
            else:
                权限='普通用户'
            root1.destroy()             #关闭容器root1
            zhujiemian()                #打开主界面

    def youke():                        #游客登录   设置权限,进入主界面
        global 用户名
        global 权限
        用户名='游客'
        权限='游客'
        root1.destroy()
        zhujiemian()

   


    root1=Frame(root,width=960,height=540)                  #在root窗口上建立虚拟容器root1,容纳登录界面的组件
    root1.pack()
    l=Label(root1,text='快递管理系统',font=('Arial',44))
    l.place(x = 270,y = 50)
    theLaber=Label(root1,text="账号:  ")
    theLaber.place(height = 20,width = 50,x = 310,y = 200)
    e1=Entry(root1)
    e1.place(height = 20,width = 200,x = 350,y = 200)
    theLaber2=Label(root1,text="密码:  ")
    theLaber2.place(height = 20,width = 50,x = 310,y = 240)
    e2=Entry(root1,show='*')
    e2.place(height = 20,width = 200,x = 350,y = 240)
    b1=Button(root1,text='登  录',command=denglu1)      #设置按钮,绑定触发的事件
    b2=Button(root1,text='注  册',command=zhuce)
    b3=Button(root1,text='游客访问',command=youke)
    b1.place(x = 310,y = 280)
    b2.place(x = 400,y = 280)
    b3.place(x = 490,y = 280)   #创立组件,并放置在容器root1上


##################################################3 main函数
root=Tk()
root.title("快递公司管理系统")
root.geometry('960x540')
denglujiemian()
root.mainloop()
'''
建立窗口root
调用登录界面函数
'''
########################################################