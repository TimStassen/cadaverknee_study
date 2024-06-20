from utils import Atlas
import os
import pdb
# first do affine transformation
# than do bpline (for more accurate results)
# check what registration is the most accurate and perform later a more thorough registration


## INITIAL IMAGE CHECK

atlas_inputs = ['17_2016', '07_2017', '30_2017']
a = Atlas(inputs = atlas_inputs)

# fix_images = ['08_2017', '10_2019']

# DEFAUT TURN ACTIVE WHEN REAL REGISTRATIONS NEED TO BE PERFORMED
fix_images = ['08_2017', '08_2017R', '10_2019', '12_2018', 
                 '18_2018', '29_2017', '01_2019']
# fix_images = ['08_2017R']


# 'fibula' is also present but not included in the registrations
anatomical_structures = ['_femur', '_tibia', '_patella'] 

fix_im_w_anatostruct = [s + ss for ss in anatomical_structures for s in fix_images]

elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
sim_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_similarity.txt'
bspline_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\Parameters_BSpline_adjusted.txt'

for image in fix_im_w_anatostruct:
    image_small = image.split('_',-1)
    image_small = image_small[0] + '_' + image_small[1]
    
    fixed_image = f'E:\\masked_scans_bone\\' + image_small + '\\' + image + '.mhd'
    fixed_mask = f'E:\segmentations PCCT Tim\masks_flip\\' + '\\' + image + '.mhd' # MASKS ARE FLIPPED, NOT IMAGES!
    atlas_path = r'E:\masked_scans_bone'
    results_path = r'E:\atlas_registration_results_bone_segs_testrun2'
    a.initialize_elastix(elastix_path, transformix_path=transformix_path, parameter_files= [sim_parameter_file, bspline_parameter_file],
                            fixed_image=fixed_image, atlas_path=atlas_path, 
                            fixed_im_mask=None, results_path=results_path)
    
    a.run_elastix()
    # a.apply_transformation()
    # a.bspline_elastix()

    # for spec_results_path in os.listdir(transformation_file_dir):

    #             transform_path = os.path.join(transformation_file_dir, spec_results_path, 'TransformParameters.1.txt') # last parameter file performed in this case
                
    #             tr_output_dir = os.path.join(transformation_file_dir, spec_results_path, 'transformix_results')
    #             if os.path.exists(tr_output_dir) is False:
    #                 os.mkdir(str(tr_output_dir))
atlas_path = r'E:\masked_scans_bone'
results_path = r'E:\atlas_registration_results_bone_segs_testrun2'

# segmentation_img_dir = r'c:\Users\T2025\Desktop\cadaver_knee_study\data\Segmentations_tim\PCCT\17_2016'

# for fix_image in fix_images:
#     for structure in anatomical_structures:

#         fixed_image = f'E:\masked_scans_bone\\' + fix_image + '\\' + fix_image + '_' + structure +'.mhd'
#         # fixed_mask = f'E:\segmentations PCCT Tim\masks_flip\\' + '\\' + fixed_image + '.mhd' # MASKS ARE FLIPPED, NOT IMAGES!
#         # pdb.set_trace()
#         a.initialize_elastix(elastix_path, transformix_path, parameter_files= [sim_parameter_file, bspline_parameter_file],
#                                 fixed_image=fixed_image, atlas_path=atlas_path, 
#                                 fixed_im_mask=None, results_path=results_path)
#         a.run_elastix()
#         # pdb.set_trace()
#         # a.apply_transformation(transformation_file_dir=results_path, segmentation_img_dir=segmentation_img_dir)
