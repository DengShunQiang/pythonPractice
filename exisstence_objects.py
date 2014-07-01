import arcpy
Workspace = "E:\pythonFile\data"
FileName =  "rivers.shp"
if arcpy.Exists("E:\pythonFile\data\\rivers.shp"):
    arcpy.Delete_management("E:\pythonFile\data\\rivers.shp")
arcpy.CreateFeatureclass_management(Workspace, FileName,"POLYLINE")
