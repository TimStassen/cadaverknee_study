
# import os
# import SimpleITK as sitk

import pymeshlab
import pdb
import numpy as np
import os
import pandas as pd

def calculate_cartilage_properties(file):

    mesh = pymeshlab.MeshSet()
    mesh.load_new_mesh(file)

    out_dict = mesh.get_geometric_measures()
    mesh_volume = out_dict['mesh_volume']
    # get the surface area
    surf_area = out_dict['surface_area']
    print('Mesh volume: \t', mesh_volume)
    # pdb.set_trace() 

    # thickness
    mesh.compute_scalar_by_shape_diameter_function_per_vertex(rays=128, cone_amplitude=30)
    m = mesh.current_mesh()
    # pdb.set_trace()
    thicknesses = m.vertex_scalar_array()
    mesh_thicknesses = [x for x in thicknesses if x<=5]
    print('mean thickness: \t', np.mean(mesh_thicknesses))

    return mesh_thicknesses, mesh_volume


if __name__ == "__main__":

    data = {}
    root_folder = r'E:\TUe_segmentations_stl'
    root_folder_dir = os.listdir(root_folder)
    for knee in root_folder_dir:
        knee_folder = os.path.join(root_folder, knee)
        modalities = os.listdir(knee_folder)
        for modality in modalities:
            modality_folder = os.path.join(knee_folder, modality)
            cartilage_files = os.listdir(modality_folder)
            for file in cartilage_files:
                file_full_path = os.path.join(modality_folder, file)
                input_name
                mesh_thickness, mesh_volume = calculate_cartilage_properties(file_full_path)
                data.setdefault(CT_name,[]).append(CT_volume)
                pdb.set_trace()



    with open(r'E:\cartilage_thickness_volumes.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])