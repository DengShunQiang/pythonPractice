# -*-  coding:utf-8  -*-
##输出PDF地图文档
import arcpy
from arcpy import env
from datetime import date

env.workspace = "E:\\pro专业学科资料\\软件工程与GIS设计"
env.overwriteOutput = True
#创建地图对象，引用当前地图
mxd = arcpy.mapping.MapDocument (u"E:\\pro专业学科资料\\软件工程与GIS设计\\sub_region.mxd")
pdfDoc=arcpy.mapping.PDFDocumentCreate(u"E:\\pro专业学科资料\\软件工程与GIS设计\\sub_region.pdf")
count=mxd.dataDrivenPages.pageCount
for pageNum in range(1,count+1):
                                       mxd.dataDrivenPages.currentPageID=pageNum
                                       row=mxd.dataDrivenPages.pageRow
                                       text_c=arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT")
                                       text_c[3].text="Author : betasy"
                                       text_c[2].text="Map of USA "+row.SUB_REGION
                                       text_c[4].text=row.describe
                                       
                                       arcpy.mapping.ExportToPDF(mxd,"E:\\pro专业学科资料\\软件工程与GIS设计\\usa.pdf")
                                       pdfDoc.insertPages("E:\\pro专业学科资料\\软件工程与GIS设计\\usa.pdf")


del mxd

