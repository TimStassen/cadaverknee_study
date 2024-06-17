from utils import Atlas
import os
import pdb
# first do affine transformation
# than do bpline (for more accurate results)
# check what registration is the most accurate and perform later a more thorough registration


## INITIAL IMAGE CHECK

atlas_inputs = ['17_2016', '07_2017', '30_2017']
a = Atlas(inputs = atlas_inputs)

# moving_images = ['08_2017', '08_2017R', '10_2019', '12_2018', 
#                  '18_2018', '29_2017', '01_2019']

moving_images = ['08_2017R']

elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
# affine_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_affine_atlas.txt'
# bspline_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_bspline_multires.txt'

registrations_dir_path = r'E:\atlas_registration_results_bone_segs6'
registrations_dir = os.listdir(registrations_dir_path)
segmentation_dir = r'E:\segmentations PCCT Tim\cartilage_PCCT_atlas_flipped3'
for registration in registrations_dir:
    # pdb.set_trace()
    parts_registration_name = registration.split('_')
    anatomical_struct = parts_registration_name[-1]
    if anatomical_struct == 'femur':
          cartilage = 'femoral_cartilage'
    elif anatomical_struct == 'tibia':
          cartilage = 'tibial_cartilage'
    elif anatomical_struct == 'patella':
          cartilage = 'retro_patellar_cartilage'
    else: 
          continue
        
    seg_img_name = parts_registration_name[2] + '_' + parts_registration_name[3]
    seg_img = os.path.join(segmentation_dir, seg_img_name, seg_img_name + '_' + cartilage + '.mhd') # or nrrd if it is not converted
    # transform_matrix0 = os.path.join(registrations_dir_path, registration, 'TransformParameters.0.txt')
    transformation_file_dir = os.path.join(registrations_dir_path, registration)

    # a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
    #                         bspline_parameter_file=bspline_parameter_file,
    #                         fixed_image=fixed_image, atlas_path=atlas_path, 
    #                         fixed_im_mask=fixed_mask, results_path=results_path)
    
    a.apply_transformation(transformation_file_dir, seg_img, fixed_image=None, moving_image=None, transformix_path=transformix_path)






# for image in moving_images:

#     fixed_image = f'E:\\ME_data_mhd\\' + image + '\\' + image + '.mhd'
#     fixed_mask = f'E:\segmentations PCCT Tim\masks_flip\\' + '\\' + image + '.mhd' # MASKS ARE FLIPPED, NOT IMAGES!
#     # pdb.set_trace()
#     atlas_path = r'E:\ME_data_mhd'
#     results_path = r'E:\atlas_registration_results_trial6'
#     a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
#                             bspline_parameter_file=bspline_parameter_file,
#                             fixed_image=fixed_image, atlas_path=atlas_path, 
#                             fixed_im_mask=fixed_mask, results_path=results_path)
#     a.affine_elastix()
#     # a.bspline_elastix()