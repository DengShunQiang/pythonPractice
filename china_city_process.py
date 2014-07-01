import sys
import arcpy
from arcpy import env
from arcpy import SpatialReference
sys.path.append("E:\pythonFile")
sys.path.append("E:\pythonFile\practiceFiles")
sys.path.append("E:\pythonFile\projects")
import china_city
input_file = open("E:\China_City.txt","r")
s= input_file.readlines()
ct=[]
city=[]
##for i in range(len(s)):
##          ct.append(s[i])
##          city[i]=china_city(ct[i][1],ct[i][2],ct[i][3])
##print city[3]
for i in range(len(s)):
          ct.append(s[i].strip('\n').strip('\"').split(","))
          
##写入到要素类
env.workspace = "E:\pythonFile\data\china_city"
env.overwriteOutput = True
city_list=[]
city_list_prj=[]
lon=[]
lat=[]
_X=[]
_Y=[]
##创建点要素类，定义坐标系统，转换坐标系统，生成新的几何对象
prosp_city=arcpy.SpatialReference("E:\pro专业学科资料\软件工程与GIS设计\China\China_prj.prj")
geosp_city=arcpy.SpatialReference("E:\pro专业学科资料\软件工程与GIS设计\China\China_geo.prj")
for c in ct:
          city_point = arcpy.Point(float(c[2]),float(c[3]))
          pointGeometry = arcpy.PointGeometry(city_point,geosp_city)
          lon.append(pointGeometry.firstPoint.X)
          lat.append(pointGeometry.firstPoint.Y)
          pointGeometry_prj=pointGeometry.projectAs(prosp_city)
          _X.append(pointGeometry_prj.firstPoint.X)
          _Y.append(pointGeometry_prj.firstPoint.Y)
          city_list.append(pointGeometry)
          city_list_prj.append(pointGeometry_prj)
arcpy.CopyFeatures_management(city_list, "cities")
arcpy.CopyFeatures_management(city_list_prj, "cities_prj")
##添加字段
arcpy.AddField_management ("cities_prj.shp","city_name","TEXT",20)
arcpy.AddField_management ("cities_prj.shp","lon","float",5,3)
arcpy.AddField_management ("cities_prj.shp","lat","float",5,3)
arcpy.AddField_management ("cities_prj.shp","X","float",5,3)
arcpy.AddField_management ("cities_prj.shp","Y","float",5,3)
arcpy.AddField_management ("cities_prj.shp","Y","float",5,3)
##为要素类赋字段值
cur = arcpy.UpdateCursor("cities_prj.shp")
i=0
for row in cur:
          row.city_name=ct[i][1]
          row.lon=ct[i][2]
          row.lat=ct[i][3]
          row.X=_X[i]
          row.Y=_Y[i]
          i=i+1
          cur.updateRow(row)
del cur,row
##任务完成
print "mission accomplished"







