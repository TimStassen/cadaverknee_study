
# import os
# import SimpleITK as sitk

import pymeshlab
import pdb
import numpy as np
import os
import pandas as pd
import xlsxwriter

def calculate_cartilage_properties(file):

    mesh = pymeshlab.MeshSet()
    mesh.load_new_mesh(file)

    out_dict = mesh.get_geometric_measures()
    # pdb.set_trace()

    if 'mesh_volume' in out_dict.keys():
        mesh_volume = out_dict['mesh_volume']
    else:
        mesh_volume = 'unable to calculate use Image information'
    # get the surface area
    # surf_area = out_dict['surface_area']
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
    # create xlsx-file
    workbook = xlsxwriter.Workbook(r'D:\Volumes_Thicknesses_cartilage.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    root_folder = r'D:\TUe_segmentations_stl'
    root_folder_dir = os.listdir(root_folder)
    for knee in root_folder_dir:
        knee_folder = os.path.join(root_folder, knee)
        modalities = os.listdir(knee_folder)
        for modality in modalities:
            modality_folder = os.path.join(knee_folder, modality)
            cartilage_files = os.listdir(modality_folder)
            for file in cartilage_files:
                file_full_path = os.path.join(modality_folder, file)
                input_name = file[:-4] + '_' + modality
                mesh_thickness, mesh_volume = calculate_cartilage_properties(file_full_path)
                # data.setdefault(input_name,[]).append(thickness)
                worksheet.write(0, 0, 'Cartilage ID')
                worksheet.write(0, 1, 'cartilage mean thickness [mm]')
                worksheet.write(0, 2, 'cartilage std thickness [mm]')
                worksheet.write(0, 3, 'cartilage volume [mm^3]')

                worksheet.write(row, 0, input_name)
                worksheet.write(row, 1, np.mean(mesh_thickness))
                worksheet.write(row, 2, np.std(mesh_thickness))
                worksheet.write(row, 3, mesh_volume)
                row+=1
                
            # pdb.set_trace()

    workbook.close()

    # with open(r'E:\cartilage_thickness_volumes.csv', 'w') as csv_file:  
    #     writer = csv.writer(csv_file)
    #     for key, value in data.items():
    #         writer.writerow([key, value])