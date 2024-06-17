import matplotlib.pyplot as plt
import numpy as np
import os
import SimpleITK as sitk
import pandas as pd
from scipy.spatial.distance import directed_hausdorff
import elastix
import random
from sklearn.metrics import confusion_matrix
from collections import Counter
import pdb

class Image_Registration:
    def __init__(self, path=None):
        # self.inputs = inputs
        self.path = path
        self.atlas_dir = None
        # self.parameter_file = None
        self.fixed_image = None
        self.fixed_im_mask = None
        self.parameter_files = None
        # self.bspline_parameter_file = None


    def include_anatomical_struct(self):
        atlas_full_paths = []
        for scan in self.atlas_list:
             
            # atlas_full_paths.append(os.path.join(self.path, scan, scan +'.mhd'))
                 
            for anatomical_struct in ['_femur', '_tibia', '_patella']:
                atlas_full_paths.append(os.path.join(self.path, scan, scan + anatomical_struct +'.mhd'))

        if 'femur' in self.fixed_image:
            atlas_full_paths_filt = [e for e in atlas_full_paths if "femur" in e]
        elif 'tibia' in self.fixed_image:
            atlas_full_paths_filt = [e for e in atlas_full_paths if "tibia" in e]
        elif 'patella' in self.fixed_image:
            atlas_full_paths_filt = [e for e in atlas_full_paths if "patella" in e]
        # elif 'fibula' in self.fixed_image:
        #     atlas_full_paths_filt = [e for e in atlas_full_paths if "fibula" in e]
        self.atlas_full_paths = atlas_full_paths_filt
        return atlas_full_paths
    
    def _correct_moving_img(self):
         if 'femur' in self.moving_img:
              a = ''
        

    
    def initialize_elastix(self, elastix_path, transformix_path, parameter_files, fixed_image, moving_image, fixed_im_mask, results_path, anatomical_structure=None):
        
        self.elastix_path = elastix_path
        self.transformix_path = transformix_path
        self.anatomical_structure = anatomical_structure

        if not os.path.exists(self.elastix_path):
            raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
        if not os.path.exists(self.transformix_path):
            raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

        self.moving_image = moving_image
        self.parameter_files = parameter_files
        self.fixed_image = fixed_image
        self.fixed_im_mask = fixed_im_mask
        self.results_path = results_path
        # self.create_atlas_dir(atlas_path)
        # self.atlas_list = self._check_L_or_R()
        # self.include_anatomical_struct()
    
    def run_elastix(self, fixed_image=None, fixed_im_mask=None, moving_image=None, image_path=None):
        # if self.atlas_full_paths is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        # elif self.parameter_files is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')         
        # elif self.fixed_image is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        
        if os.path.exists(self.results_path) is False:
                os.mkdir(str(self.results_path))
        self.results_list = []
        if fixed_image is None:
            fixed_image = self.fixed_image.split('\\')[-1]
            fixed_image = fixed_image[:-4]
            moving_image = self.moving_image.split('\\')[-1]
            moving_image = moving_image[:-4]
            # pdb.set_trace()
            # for moving_image in self.atlas_list:
            #     spec_results_path = os.path.join(self.results_path, 'atlas_img_' + moving_image + '_fixed_'+ fixed_image)
            #     self.results_list.append(spec_results_path)
            #     full_path_moving_im = [i for i in self.atlas_full_paths if moving_image in i][0]

            #     # pdb.set_trace()
            #     # self._check_moving_paths()

            #     print('moving image: \t' + moving_image)
            #     print(full_path_moving_im)
            spec_results_path = os.path.join(self.results_path, moving_image)
            if os.path.exists(spec_results_path) is False:
                os.mkdir(str(spec_results_path))
            el = elastix.ElastixInterface(elastix_path=self.elastix_path)
            el.register(
                fixed_image=self.fixed_image,
                fixed_mask=self.fixed_im_mask,
                moving_image=self.moving_image,
                parameters=self.parameter_files,
                output_dir=spec_results_path)
                    
                

        # elif isinstance(fixed_image, str):
        #         spec_results_path = os.path.join(self.results_path, 'moving_img_' + moving_image[:-4] + '_fixed_' + fixed_image[:-4])
        #         self.results_list.append(spec_results_path)
        #         full_path_moving_im = os.path.join(image_path, moving_image[:-4], moving_image) # wil not work for .nrrd files
        #         full_path_fixed_im = os.path.join(image_path, fixed_image[:-4], fixed_image)

        #         if os.path.exists(spec_results_path) is False:
        #             os.mkdir(str(spec_results_path))

        #         print('moving image: \t' + moving_image)

        #         el = elastix.ElastixInterface(elastix_path=self.elastix_path)
        #         el.register(
        #             fixed_image=full_path_fixed_im,
        #             fixed_mask=fixed_im_mask,
        #             moving_image=full_path_moving_im,
        #             parameters=self.parameter_files,
        #             output_dir=spec_results_path)
                

        else:
            print('Elastix was not used, check the input variable or for bugs in the code')
        


    def apply_transformation(self, transformation_file_dir, segmentation_img, fixed_image=None, moving_image=None, transformix_path=None):
        # transformix
        # if registratons have been done in the same operation, self.results_list can be used, otherwise the path has to be specified
            # for spec_results_path in os.listdir(transformation_file_dir):
                if transformix_path == None:
                    #  if self.transformix_path == None:
                    # assert 'No transformix path defined! Add this in transformix_path=... or during initialization'
                    #  else:
                        transformix_path = self.transformix_path
                
                transform_file1 = os.path.join(transformation_file_dir, 'TransformParameters.0.txt') # last parameter file performed in this case
                
                tr_output_dir1 = os.path.join(transformation_file_dir, 'transformix_results0')
                if os.path.exists(tr_output_dir1) is False:
                    os.mkdir(str(tr_output_dir1))
                # pdb.set_trace()
                # pdb.set_trace()
                # make code indicating what knee tructure it is:
                # knee_struct = spec_results_path.split("_",3)[-1].split("_",4)  
                # pdb.set_trace()
            
                tr = elastix.TransformixInterface(parameters=transform_file1, transformix_path=transformix_path)
                tr.transform_image(image_path = segmentation_img, output_dir=tr_output_dir1)

    def show_evaluation(self):

        return None

if __name__ == "__main__":
    # atlas_inputs = ['17_2016', '07_2017', '30_2017']
    a = Image_Registration()

    elastix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\elastix.exe')
    transformix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\transformix.exe')
    affine_parameter_file = r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\cadaver_knee_study2\code\elastix_parameter_files\parameters_MR_pcct.txt'
    fixed_image = r"D:\segmentations MR Tim\07_2017\07_2017_femoral_cartilage.nrrd" #MR
    # fixed_mask = r'D:\segmentations PCCT Tim\masks\01_2019.nrrd' # FILL IN PATH TO .nrrd FILE
    moving_image = r"D:\TUe_segmentations_PCCT\07_2017\07_2017_femoral_cartilage.nrrd" #PCCT
    # moving_image = r"D:\ME_data_mhd\07_2017\07_2017.mhd" #PCCT
    results_path = r'D:\registration_results_test17'
    a.initialize_elastix(elastix_path, transformix_path, 
                         parameter_files=[affine_parameter_file], 
                         fixed_image=fixed_image, moving_image=moving_image, 
                         fixed_im_mask=None, results_path=results_path,
                        #  anatomical_structure='femur'
                         )
    # a.run_elastix(fixed_image='12_2018_femur.mhd', moving_image='17_2016_femur.mhd', image_path=r'D:\masked_scans_bone')
    a.run_elastix()


    segmentation_path = r'D:\TUe_segmentations_PCCT\07_2017' # PCCT
    segmentation_dir = os.listdir(segmentation_path)
    results_dir = os.listdir(results_path)
    for registration in results_dir:
        
        parts_registration_name = registration.split('_')
        anatomical_struct = parts_registration_name[-1]
        if anatomical_struct == 'femur':
            cartilage = 'femoral_cartilage'
        elif anatomical_struct == 'tibia':
            cartilage = 'tibial_cartilage'
        elif anatomical_struct == 'patella':
            cartilage = 'retro_patellar_cartilage'
        else: 
            cartilage = ''
        knee = parts_registration_name[0] + '_' + parts_registration_name[1]
        seg_img_name = parts_registration_name[0] + '_' + parts_registration_name[1] # + '_' + 'femoral_cartilage'
        # seg_img = os.path.join(segmentation_path, seg_img_name + '.nrrd') # or nrrd if it is not converted
        seg_img =os.path.join(segmentation_path, seg_img_name + '_femoral_cartilage.nrrd') # or nrrd if it is not converted
        # transform_matrix0 = os.path.join(registrations_dir_path, registration, 'TransformParameters.0.txt')
        transformation_file_dir = os.path.join(results_path, registration)
        # pdb.set_trace()   
        # a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
        #                         bspline_parameter_file=bspline_parameter_file,
        #                         fixed_image=fixed_image, atlas_path=atlas_path, 
        #                         fixed_im_mask=fixed_mask, results_path=results_path)
        
        a.apply_transformation(transformation_file_dir, seg_img, fixed_image=None, moving_image=None, transformix_path=transformix_path)