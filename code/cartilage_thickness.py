import pymeshlab
import numpy as np

mesh = pymeshlab.MeshSet()
mesh.load_new_mesh(r"D:\TUe_segmentations_stl\30_2017\30_2017_femoral_cartilage.stl")
mesh.compute_scalar_by_shape_diameter_function_per_vertex(rays=64, cone_amplitude=30)

m = mesh.current_mesh()
thickness = m.vertex_scalar_array()
thickness = [x for x in thickness if x <= 5]
print('mean thickness: \t',  np.mean(thickness))