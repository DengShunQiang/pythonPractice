# Name: IDW_ca_pm10_pts.py
# Description: Interpolate a series of point features onto a rectangular 
#   raster using Inverse Distance Weighting (IDW).
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "E:\\MGIS\\mgisdata\\ca"
env.overwriteOutput = True
desc = arcpy.Describe("ca_outline.shp")
env.extent = desc.extent

# Set Mask environment
arcpy.env.mask = "E:\\MGIS\\mgisdata\\ca\\ca_outline.shp"
# Set local variables
inPointFeatures = "E:\\MGIS\\mgisdata\\ca\\ca_pm10_pts.shp"
zField = "ELEVATION"
zField2="PM10AGM"
cellSize = 2000
distance = 15000
minNumPoints=3
searchRadius = RadiusFixed(distance, minNumPoints)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute IDW
outIDW = Idw(inPointFeatures, zField,cellSize, "", searchRadius)
outIDW2 = Idw(inPointFeatures,zField2,cellSize, "", searchRadius)
# Save the output 
outIDW.save("elev")
outIDW2.save("pm10")

