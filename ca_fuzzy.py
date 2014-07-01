# Name: FuzzyMembership_ca.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
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
# Set Local Variables
inRaster1 = "distance"
inRaster2 = "pm10"
inRaster3 = "elev"
# Create the FuzzyGaussian algorithm object
midpoint = 20000
spread = 0.5
min = 0
max = 1
myFuzzyAlgorithm1 = FuzzySmall(midpoint, spread)
myFuzzyAlgorithm2 = FuzzySmall()
myFuzzyAlgorithm3 = FuzzyLinear(min, max)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute FuzzyMembership
outFuzzyMember1 = FuzzyMembership(inRaster1, myFuzzyAlgorithm1)
outFuzzyMember2 = FuzzyMembership(inRaster2, myFuzzyAlgorithm2)
outFuzzyMember3 = FuzzyMembership(inRaster3, myFuzzyAlgorithm3)

# Save the output
outFuzzyMember1.save("E:\\MGIS\\mgisdata\\ca\\fzy_distance")
outFuzzyMember2.save("E:\\MGIS\\mgisdata\\ca\\fzy_elev")
outFuzzyMember3.save("E:\\MGIS\\mgisdata\\ca\\fzy_pm10")
