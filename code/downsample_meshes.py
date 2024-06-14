import trimesh as tm
import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb
import pyvista as pv
import vtk 


#

# load mesh
my_pyvista_mesh = pv.read(r"D:\TUe_segmentations_stl\30_2017\30_2017_femoral_cartilage.stl")

specific_vtk_filter = vtk.vtkQuadricDecimation()
specific_vtk_filter.SetTargetReduction(.9)

# this works
specific_vtk_filter.SetInputData(my_pyvista_mesh)
specific_vtk_filter.Update()
down_sampled_mesh = specific_vtk_filter.GetOutput()


p = pv.Plotter()
p.add_mesh(down_sampled_mesh)
p.show()

m = vtk.vtkMassProperties()
m.SetInputData(down_sampled_mesh)
print(m.GetVolume())
print(m.GetSurfaceArea())
pdb.set_trace()

# down_sampled_mesh.save(r"D:\TUe_segmentations_stl\30_2017\30_2017_femoral_cartilage_DOWNSAMPLED.stl", binary=True)
# pdb.set_trace()

stlWriter = vtk.vtkSTLWriter()
stlWriter.SetFileName(r"D:\TUe_segmentations_stl\30_2017\30_2017_femoral_cartilage_DOWNSAMPLED.stl")
stlWriter.SetInputData(down_sampled_mesh)
stlWriter.Update()
stlWriter.Write()

# # this fails
# specific_vtk_filter.SetInputConnection(my_pyvista_mesh)