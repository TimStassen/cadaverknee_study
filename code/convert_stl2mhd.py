from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import pdb

# Using an existing stl file

# Create a new plot
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file(r'E:\segmentations PCCT Tim\bone_segs\12_2018\Segmentation_femur.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()

# pdb.set_trace()