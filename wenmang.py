# -*-  coding:cp936  -*-
# -*-  coding:utf-8  -*-
#������ʾ��һ������û�н����ֻ����Ӣ�Ĵ���������������
from xlrd import *
import xlwt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
wenmang=open_workbook("E:\\proרҵѧ������\\���������GIS���\\��ä��.xlsx")
wenmang1 = wenmang.sheets()[0]#����һ��sheet����wenmang1
rate=wenmang1.col_values(1)
province=wenmang1.col_values(0)#�����ä�ʺ�ʡ��
rate1=rate[1:32]
province1=province[1:32]#ȥ����һ���ֶ����ݣ�ֻ��������
data=[]
for i in range(31):
        data.append([province1[i],rate1[i]])  #��ʡ�ݺ���ä��һһ��Ӧ����
sorted_data=sorted(data,key = lambda data:data[1],reverse=True)#������ä��ֵ��С����
sorted_data0=[]
sorted_data1=[]
e=[]#���ں������ǩ����
for j in range(len(sorted_data)):
        e.append(j)
        sorted_data0.append(sorted_data[j][0])
        sorted_data1.append(sorted_data[j][1])#�ֱ����б�洢���ݣ����ڻ�ͼ
fig=plt.figure()
ax=fig.add_subplot(111)
plt.bar(e,sorted_data1,width=0.5,color="r",align="center")#������״ͼ
font= FontProperties(fname="c:\\windows\\fonts\\AdobeFangsongStd-Regular.otf")
ax.set_xlabel(u'ʡ��',fontproperties=font,fontsize=18)
ax.set_ylabel(u'��ä��(%)',fontproperties=font,fontsize=18)#����x,y��ʾ����
plt.xticks(e,sorted_data0,rotation=60)
ax.set_xticklabels(sorted_data0,fontproperties=font,fontsize=14)#���ú���̶ȱ��
plt.title(u'2010��ʡ��ä��',fontproperties=font,fontsize=18)#����ͼ�����
plt.show()
plt.savefig("C:\\Python27\\tmp\\fig1.png",dpi=120)#��ʾ�ͱ���ͼƬ
print "mission accomplished"

        






