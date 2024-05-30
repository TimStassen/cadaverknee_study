from utils import Atlas
import os
import pdb
# first do affine transformation
# than do bpline (for more accurate results)
# check what registration is the most accurate and perform later a more thorough registration


## INITIAL IMAGE CHECK

atlas_inputs = ['17_2016', '07_2017', '30_2017']
a = Atlas(inputs = atlas_inputs)

moving_images = ['08_2017', '08_2017R', '10_2019', '12_2018', 
                 '18_2018', '29_2017', '01_2019']

# 'fibula' is also present but not included in the registrations
anatomical_structures = ['femur', 'tibia', 'patella'] 

elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
sim_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_similarity.txt'
bspline_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\Parameters_BSpline_adjusted.txt'

atlas_path = r'E:\masked_scans_bone'
results_path = r'E:\atlas_registration_results_bone_segs'

# segmentation_img_dir = r'c:\Users\T2025\Desktop\cadaver_knee_study\data\Segmentations_tim\PCCT\17_2016'

for moving_image in moving_images:
    for structure in anatomical_structures:

        fixed_image = f'E:\masked_scans_bone\\' + moving_image + '\\' + moving_image + '_' + structure +'.mhd'
        # fixed_mask = f'E:\segmentations PCCT Tim\masks_flip\\' + '\\' + fixed_image + '.mhd' # MASKS ARE FLIPPED, NOT IMAGES!
        # pdb.set_trace()
        a.initialize_elastix(elastix_path, transformix_path, parameter_files= [sim_parameter_file, bspline_parameter_file],
                                fixed_image=fixed_image, atlas_path=atlas_path, 
                                fixed_im_mask=None, results_path=results_path)
        a.run_elastix()
        # pdb.set_trace()
        # a.apply_transformation(transformation_file_dir=results_path, segmentation_img_dir=segmentation_img_dir)