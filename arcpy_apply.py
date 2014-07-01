import arcpy
from arcpy import env
environments = arcpy.ListEnvironments()
for environment in environments:
    envSetting = eval("env." + environment)
    print "%-28s: %s" % (environment, envSetting)
