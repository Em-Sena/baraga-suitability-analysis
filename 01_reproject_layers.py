import arcpy
import os
#Set the workspace
arcpy.env.workspace=r"D:\2026\Baraga\Baraga.gdb"
output_folder=r"D:\2026\Baraga\Baraga.gdb"
#Michigan Georeference
target_sr=arcpy.SpatialReference(3078)
#to get List of feature classes
fc_list=arcpy.ListFeatureClasses()
print(f"Starting reprojectionif {len(fc_list)}layers...")
for fc in fc_list:
    out_feature=os.path.join(output_folder,f"{fc}_Projected")
    try:
        arcpy.management.Project(fc,out_feature,target_sr)
        print(f"Successfully projected:{fc}")
    except Exception as e:
        print(f"Failed to project{fc}:{e}")
print("Done")
