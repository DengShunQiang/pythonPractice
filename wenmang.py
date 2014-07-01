# -*-  coding:cp936  -*-
# -*-  coding:utf-8  -*-
#中文显示有一点问题没有解决，只好用英文代替标题坐标的中文
from xlrd import *
import xlwt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
wenmang=open_workbook("E:\\pro专业学科资料\\软件工程与GIS设计\\文盲率.xlsx")
wenmang1 = wenmang.sheets()[0]#生成一个sheet对象wenmang1
rate=wenmang1.col_values(1)
province=wenmang1.col_values(0)#存放文盲率和省份
rate1=rate[1:32]
province1=province[1:32]#去掉第一行字段内容，只保存数据
data=[]
for i in range(31):
        data.append([province1[i],rate1[i]])  #把省份和文盲率一一对应起来
sorted_data=sorted(data,key = lambda data:data[1],reverse=True)#按照文盲率值大小排序
sorted_data0=[]
sorted_data1=[]
e=[]#用于横坐标标签排列
for j in range(len(sorted_data)):
        e.append(j)
        sorted_data0.append(sorted_data[j][0])
        sorted_data1.append(sorted_data[j][1])#分别用列表存储数据，便于画图
fig=plt.figure()
ax=fig.add_subplot(111)
plt.bar(e,sorted_data1,width=0.5,color="r",align="center")#绘制柱状图
font= FontProperties(fname="c:\\windows\\fonts\\AdobeFangsongStd-Regular.otf")
ax.set_xlabel(u'省份',fontproperties=font,fontsize=18)
ax.set_ylabel(u'文盲率(%)',fontproperties=font,fontsize=18)#设置x,y显示标题
plt.xticks(e,sorted_data0,rotation=60)
ax.set_xticklabels(sorted_data0,fontproperties=font,fontsize=14)#设置横轴刻度标记
plt.title(u'2010分省文盲率',fontproperties=font,fontsize=18)#设置图像标题
plt.show()
plt.savefig("C:\\Python27\\tmp\\fig1.png",dpi=120)#显示和保存图片
print "mission accomplished"

        






