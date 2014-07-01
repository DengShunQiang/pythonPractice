# encoding ="utf-8"
# Name: landuse.py
# Description: calculate landuse statistics and draw graphs
# Author: 10111710326 邓顺强
import sys
sys.path.append("D:\应用程序\arcgis10.1\ArcGIS10.1\Lib\site-packages\matplotlib")
# import system modules 
import arcpy 
from arcpy import env
##import matplotlib.pyplot as plt

# Set environment settings
env.workspace = "E:\\MGIS\\mgisdata\\shanghai1"
env.overwriteOutput =True
# Split landuse layer by district NAME, write to dataset shanghai1
in_features = "landuse.shp"
split_features = "districts.shp"
split_field = "NAME"
out_workspace = "E:\\MGIS\\mgisdata\\shanghai1"
#clusterTol = "1 Meters"
arcpy.Split_analysis (in_features, split_features, split_field, out_workspace)
# landuse sum statistics in subregion
arcpy.Statistics_analysis ("卢湾区.shp", "E:\\MGIS\\mgisdata\\shanghai1\\卢湾.dbf", [["AREA","SUM"]],"type")
arcpy.Statistics_analysis ("静安区.shp", "E:\\MGIS\\mgisdata\\shanghai1\\静安.dbf", [["AREA","SUM"]],"type")
arcpy.Statistics_analysis ("黄浦区.shp", "E:\\MGIS\\mgisdata\\shanghai1\\黄浦.dbf", [["AREA","SUM"]],"type")
#draw histograms
import matplotlib.pyplot as plt
input_=["E:\\MGIS\\mgisdata\\shanghai1\\卢湾.dbf","E:\\MGIS\\mgisdata\\shanghai1\\静安.dbf","E:\\MGIS\\mgisdata\\shanghai1\\黄浦.dbf"]
name=["卢湾区","静安区","黄浦区"]
for i in range(len(input_)):
    cur=arcpy.SearchCursor (i)
land_type=[],value=[]
    for row in cur:
        land_type.append(row.type)
        value.append(row.SUM_AREA)
    plt.bar([1,2,3,4,5,6],value,width=0.5,color="r")
    plt.show()
    plt.savefig("E:\\MGIS\\mgisdata\\shanghai1\\"+name[i]+".png")
    plt.clf()
    del cur,row


