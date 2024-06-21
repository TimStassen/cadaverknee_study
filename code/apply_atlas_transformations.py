from utils import Atlas
import os
import pdb

""" Apply the transformation performed on the segmentation masks"""


atlas_inputs = ['17_2016', '07_2017', '30_2017']
a = Atlas(inputs = atlas_inputs)

moving_images = ['08_2017', '08_2017R', '10_2019', '12_2018', 
                 '18_2018', '29_2017', '01_2019']


elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')

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
    transformation_file_dir = os.path.join(registrations_dir_path, registration)
    
    a.apply_transformation(transformation_file_dir, seg_img, fixed_image=None, moving_image=None, transformix_path=transformix_path)


