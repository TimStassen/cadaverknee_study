from utils import Image_Registration
import os
import pdb

root_MR_dir = r"E:\segmentations MR Tim"
root_PCCT_dir = r"E:\TUe_segmentations_PCCT"

# root_MR_dir = r"E:\TUe_masked_MR"
# root_PCCT_dir = r"E:\segmentations PCCT Tim\bone_segs\nrrd"

results_path = r"E:\registration_results_FINAL4"

elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
affine_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_MR_pcct.txt'

included_knees = ['07_2017', '17_2016', '18_2018', '30_2017']
# included_structures = ['femur', 'patella', 'tibia']
included_structures = ['femoral_cartilage', 'tibial_cartilage', 'retro_patellar_cartilage']
 
# loop over all files
for knee in included_knees:
    MR_knee_folder = os.path.join(root_MR_dir, knee)
    PCCT_knee_folder = os.path.join(root_PCCT_dir, knee)

    for struct in included_structures:
        MR_knee_file = knee + '_' + struct + '.nrrd'
        MR_knee_full_path = os.path.join(MR_knee_folder, MR_knee_file)

        PCCT_knee_file = knee + '_' + struct + '.nrrd'
        PCCT_knee_full_path = os.path.join(PCCT_knee_folder, PCCT_knee_file)

        fixed_image = MR_knee_full_path
        moving_image = PCCT_knee_full_path

        # pdb.set_trace()
        # print('fixed_image: \t', fixed_image, '\n moving image: \t', moving_image)
# -------------------------------------------START REGISTRATION PART--------------------------------------------------
        a = Image_Registration()

        a.initialize_elastix(elastix_path, transformix_path, 
                         parameter_files=[affine_parameter_file], 
                         fixed_image=fixed_image, moving_image=moving_image, 
                         fixed_im_mask=None, results_path=results_path,
                        #  anatomical_structure='femur'
                         )
        a.run_elastix()


        root_segmentation_path = r'E:\TUe_segmentations_PCCT' # PCCT

        if struct == 'femur' or struct == 'femoral_cartilage':
            cartilage = 'femoral_cartilage'
            segmentation_file = os.path.join(root_segmentation_path, knee, knee + '_' + cartilage + '.nrrd')
        elif struct == 'tibia' or struct == 'tibial_cartilage':
            cartilage = 'tibial_cartilage'
            segmentation_file = os.path.join(root_segmentation_path, knee, knee + '_' + cartilage + '.nrrd')
        elif struct == 'patella' or struct == 'retro_patellar_cartilage':
            cartilage = 'retro_patellar_cartilage'
            segmentation_file = os.path.join(root_segmentation_path, knee, knee + '_' + cartilage + '.nrrd')
        else: 
            ValueError('No valid input file is given. Must be femur, patella or tibia')
        
        # pdb.set_trace()
        transformation_file_dir = os.path.join(results_path, knee + '_' + struct)
        a.apply_transformation(transformation_file_dir, segmentation_file, transformix_path=transformix_path)
        # pdb.set_trace()



        # segmentation_dir = os.listdir(segmentation_path)
        # results_dir = os.listdir(results_path)
        # for registration in results_dir:
            

        #     knee = parts_registration_name[0] + '_' + parts_registration_name[1]
        #     seg_img_name = parts_registration_name[0] + '_' + parts_registration_name[1] # + '_' + 'femoral_cartilage'
        #     # seg_img = os.path.join(segmentation_path, seg_img_name + '.nrrd') # or nrrd if it is not converted
        #     seg_img =os.path.join(segmentation_path, seg_img_name + '_tibial_cartilage.nrrd') # or nrrd if it is not converted
        #     # transform_matrix0 = os.path.join(registrations_dir_path, registration, 'TransformParameters.0.txt')
        #     transformation_file_dir = os.path.join(results_path, registration)
        #     # pdb.set_trace()   
        #     # a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
        #     #                         bspline_parameter_file=bspline_parameter_file,
        #     #                         fixed_image=fixed_image, atlas_path=atlas_path, 
        #     #                         fixed_im_mask=fixed_mask, results_path=results_path)
            
        #     a.apply_transformation(transformation_file_dir, seg_img, fixed_image=None, moving_image=None, transformix_path=transformix_path)
