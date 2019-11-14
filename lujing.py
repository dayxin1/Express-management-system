from sqlml import Sql          #导入自定义模块sqlML中的类Sql
import math
# chengshi=[]       # 城市 (chengshi) 列表来保存路径



def lujing2(chufa,mudi,chengshi):   #输入出发与到达市,通过递归  贪心算法  计算出最短路径   只供 lujing()调用
   sqlm="select 省会城市 from 邻接表 where " + chufa + "=1"  #编辑sql命令
   xlcs=Sql.sql1(sqlm)
   #print(chufa,'-',mudi,"附近的城市",xlcs)####################################################################################################################33
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
   sqlm="select 经度,纬度 from 市表 where 市名 ='" + mudi+"'"
   jwd0=Sql.sql1(sqlm)                           #目的地经纬度

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
   juli=0                                    #初始化两城市之间距离,算法为经度纬度的差值
   chengshi2="0"                             #初始化出发城市最近的城市.用来保存最近城市的变量
   for x in xlcs:          #  遍历附近的城市                   #获取附近城市经纬度,比较哪个离目的地最近,如果是目的城市,直接跳出
      sqlm="select 经度,纬度 from 市表 where 市名 ='" + x[0]+"'"
      jwd=Sql.sql1(sqlm)
      a =  float(jwd[0][0]) - float(jwd0[0][0])
      b =  float(jwd[0][1]) - float(jwd0[0][1])
      juli2 = math.sqrt(pow(a,2)+pow(b,2))
      if x[0]==mudi:
         chengshi2=x[0] 
         break
      elif juli2 < juli or juli==0: 
         juli=juli2
         chengshi2=x[0]  

   if chengshi2 == mudi:                  #如果最近的城市就是目的城市,结束递归,将目的城市添加到路径末尾
      chengshi+=chengshi2, 
      return chengshi
   else:
      chengshi+=chengshi2,                #不是,将中间城市添加到路径,递归运算
      chengshi=lujing2(chengshi2,mudi,chengshi)
      return chengshi



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def lujing(chufa,mudi):                  #函数功能是输入2省 计算出最优路径
   if chufa==mudi:                        #如果是本省快递,返回0
      return ('0',)
   else:                                  #不是本省快递,调用lujing2计算最优路径
      sqlm="select 省会城市 from 省份表 where 省份='"+chufa+"'"
      shcs=Sql.sql1(sqlm)                             #shcs 省会城市



      sqlm="select 省会城市 from 省份表 where 省份='"+mudi+"'"
      shcs2=Sql.sql1(sqlm)                              #shcs 省会城市

 
      chengshi=shcs[0][0],                         #将出发城市添加到路径表的第一位
     # print(shcs,shcs2) #############################################################################################33
      chengshi= lujing2(shcs[0][0],shcs2[0][0],chengshi) #调用函数 计算最短路径列表
    
      return chengshi
   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
  

chengshi=lujing('安徽','安徽')
print(chengshi)