import trimesh as tm
import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pyvista
import vtk 

# mask_path = r"D:\segmentations MR Tim\30_2017_v2\30_2017_tibial_cartilage.nrrd"

# itk_mask = sitk.ReadImage(mask_path)
# mask_array = sitk.GetArrayViewFromImage(itk_mask)
# pdb.set_trace()
# mesh = tm.Trimesh(vertices=mask_array,
#                     faces=[[0, 1]]
                    # )

mesh = tm.load(r"D:\TUe_segmentations_stl\30_2017\30_2017_femoral_cartilage_DOWNSAMPLED.stl")   
# mesh = tm.load(r"C:\Users\20201900\Downloads\20mm_cube.stl") 
# mesh.vertices = mesh.vertices[::10] # takes one in 10 start_points
# mesh.faces = mesh.faces[::10]
  

start_points = mesh.vertices - 0.00001 * mesh.vertex_normals # hacky way to get points slightly inside
# start_points = mesh.vertices
# down_sampled_start_points = start_points[::10] # takes one in 10 start_points

thickness = tm.proximity.thickness(mesh,start_points, normals=mesh.vertex_normals
                                   ) # method='ray'
pdb.set_trace()
import pyvista as pv
pv.wrap(mesh).plot(scalars=thickness)

# pdb.set_trace()
