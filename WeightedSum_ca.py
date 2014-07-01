# Name: WeightedSum_ca.py
# Description: Overlays several rasters multiplying each by their given
#    weight and summing them together.
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
inRaster1 = "fzy_distance"
inRaster2 = "fzy_elev"
inRaster3 = "fzy_pm10"
WSumTableObj = WSTable([[inRaster1, "VALUE", 0.2], [inRaster2, "VALUE", 0.5],
                        [inRaster3, "VALUE", 0.3]])

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute WeightedSum
outWeightedSum = WeightedSum(WSumTableObj)

# Save the output 
outWeightedSum.save("E:\\MGIS\\mgisdata\\ca\\wsumca")
