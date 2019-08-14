


import arcpy
import os
import sys
from arcpy import env
import glob

folderPath=arcpy.GetParameterAsText(0) ##Enter path to folder where .mxd files are located
env.workspace=folderPath
mxdList = [os.path.join(root, name)
             for root, dirs, files in os.walk(folderPath)
             for name in files
             if name.endswith((".mxd"))]
arcpy.AddMessage(mxdList)
#mxdList=arcpy.ListFiles("*.mxd")
#print mxdList
for mxd in mxdList:
    mapobject=arcpy.mapping.MapDocument(mxd)#(folderPath + '\\' + mxd)
    arcpy.AddMessage(mapobject)
    #print mapobject
    try:
        for df in arcpy.mapping.ListDataFrames(mapobject):
            print (df)
            for lyr in arcpy.mapping.ListLayers(mapobject, "", df):
                print (lyr)
                if lyr.isRasterLayer:
                    if lyr.isServiceLayer:
                        arcpy.mapping.RemoveLayer(df, lyr)
                        arcpy.AddMessage("Layer Removed")
                        #print 'Layer Removed'
        arcpy.RefreshTOC()
        mapobject.save()

    except:
        print ('Failed to Remove')

del mapobject
