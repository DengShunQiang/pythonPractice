# Name: EucDistance_ca_cities.py
# Description: Calculates for each cell the Euclidean distance to the nearest source.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "E:\MGIS\mgisdata\ca"
# Set Mask environment
arcpy.env.mask = "E:\MGIS\mgisdata\ca\ca_outline.shp"
env.overwriteOutput = True
# Set local variables
inSourceData = "E:\\MGIS\\mgisdata\\ca\\ca_cities.shp"
maxDistance = 4000
cellSize = 2
outDirectionRaster = "E:\\MGIS\\mgisdata\\ca\\distance"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute EucDistance
outEucDistance = EucDistance(inSourceData, "", "", outDirectionRaster)

# Save the output 
outEucDistance.save("E:\\MGIS\\mgisdata\\ca\\distance")


