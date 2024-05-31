from utils import Atlas
import os
import pdb
# first do affine transformation
# than do bpline (for more accurate results)
# check what registration is the most accurate and perform later a more thorough registration


## INITIAL IMAGE CHECK

atlas_inputs = ['17_2016', '07_2017', '30_2017']
a = Atlas(inputs = atlas_inputs)

fix_images = ['08_2017', '08_2017R', '10_2019', '12_2018', 
                 '18_2018', '29_2017', '30_2017']

elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
affine_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_affine_atlas.txt'
bspline_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_bspline_multires.txt'

for image in fix_images:

    fixed_image = f'E:\\ME_data_mhd\\' + image + '\\' + image + '.mhd'
    fixed_mask = f'E:\segmentations PCCT Tim\masks_flip\\' + '\\' + image + '.mhd' # MASKS ARE FLIPPED, NOT IMAGES!
    # pdb.set_trace()
    atlas_path = r'E:\ME_data_mhd'
    results_path = r'E:\atlas_registration_results_trial6'
    a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
                            bspline_parameter_file=bspline_parameter_file,
                            fixed_image=fixed_image, atlas_path=atlas_path, 
                            fixed_im_mask=fixed_mask, results_path=results_path)
    a.apply_transformation()
    # a.bspline_elastix()

    # for spec_results_path in os.listdir(transformation_file_dir):

    #             transform_path = os.path.join(transformation_file_dir, spec_results_path, 'TransformParameters.1.txt') # last parameter file performed in this case
                
    #             tr_output_dir = os.path.join(transformation_file_dir, spec_results_path, 'transformix_results')
    #             if os.path.exists(tr_output_dir) is False:
    #                 os.mkdir(str(tr_output_dir))
