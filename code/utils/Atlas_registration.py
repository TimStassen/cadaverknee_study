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

class Atlas:
    def __init__(self, inputs, path=None):
        self.inputs = inputs
        self.path = path
        self.atlas_dir = None
        # self.parameter_file = None
        self.fixed_image = None
        self.fixed_im_mask = None
        self.parameter_files = None
        # self.bspline_parameter_file = None


    def _check_atlas_codes(self):
        # if self.inputs is not list:
        #     return f"{self.inputs} must be a list"
        
        all_scan_codes = ['01_2019', '07_2017', '08_2017', '08_2017R', '10_2019', 
                          '12_2018', '17_2016', '18_2018', '29_2017', '30_2017']
        atlas_list = []
        for scan_code in self.inputs:
            # pdb.set_trace()
            if scan_code in all_scan_codes:
                   atlas_list.append(scan_code)
            # pdb.set_trace()
            assert scan_code in all_scan_codes, f"{scan_code} is an invalid entry, check for typos"

        self.atlas_list = atlas_list
        return self.atlas_list
    
    def _check_L_or_R(self):
        # !! only applicable for the atlas_images: '07_2017' (right), '17_2016' (left), '30_2017' (left) !!



        if self.fixed_image == '01_2019':       # right-sided knee
            # self.atlas_list.remove('17_2016')
            # self.atlas_list.remove('30_2017')
            self.atlas_list = [e for e in self.atlas_list if e not in ('17_2016', '30_2017')]
        elif self.fixed_image == '08_2017':     # left-sided knee
            self.atlas_list.remove('07_2017')
        elif self.fixed_image == '08_2017R':
            self.atlas_list = [e for e in self.atlas_list if e not in ('17_2016', '30_2017')]
        elif self.fixed_image == '10_2019':
            self.atlas_list = [e for e in self.atlas_list if e not in ('17_2016', '30_2017')]
        elif self.fixed_image == '12_2018':
            self.atlas_list = [e for e in self.atlas_list if e not in ('17_2016', '30_2017')]
        elif self.fixed_image == '18_2018':
            self.atlas_list = [e for e in self.atlas_list if e not in ('17_2016', '30_2017')]
        elif self.fixed_image == '29_2017':
            self.atlas_list.remove('07_2017')

        return self.atlas_list
    
    def _check_anatomical_ROI(self):
         if self.anatomical_structure == 'femur':
              self.atlas_list = [s + '_femur' for s in self.atlas_list]
         elif self.anatomical_structure == 'patella':
              self.atlas_list = [s + '_patella' for s in self.atlas_list]
         elif self.anatomical_structure == 'tibia':
              self.atlas_list = [s + '_tibia' for s in self.atlas_list]
        
        # if scan in all_scan_codes for scan in all_scan_codes.inputs:
    def create_atlas_dir(self, path=None):
        if path is None and self.path is None:
            return f"Variable: 'path', is not defined"
        elif path is None:
            path = self.path

        elif self.path is None:
            self.path = path

        self.atlas_list = self._check_atlas_codes()
        self._check_anatomical_ROI()

        atlas_full_paths = []
        for scan in self.atlas_list:
            atlas_full_paths.append(os.path.join(self.path, scan+'.mhd'))
        
        self.atlas_full_paths = atlas_full_paths
        
        return self.atlas_full_paths
    
    def initialize_elastix(self, elastix_path, transformix_path, parameter_files, fixed_image, atlas_path, fixed_im_mask, results_path, anatomical_structure=None):
        
        self.elastix_path = elastix_path
        self.transformix_path = transformix_path
        self.anatomical_structure = anatomical_structure

        if not os.path.exists(self.elastix_path):
            raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
        if not os.path.exists(self.transformix_path):
            raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

        # self.atlas_dir = self.create_atlas_dir(atlas_path)
        # pdb.set_trace()
        
        
        self.atlas_dir = self.create_atlas_dir(atlas_path)
        self.atlas_list = self._check_L_or_R()
        self.parameter_files = parameter_files
        self.fixed_image = fixed_image
        self.fixed_im_mask = fixed_im_mask
        self.results_path = results_path
        
    
        

    def run_elastix(self, fixed_image=None, fixed_im_mask=None, moving_image=None, image_path=None):
        if self.atlas_dir is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        elif self.parameter_files is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')         
        elif self.fixed_image is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        # elif self.fixed_im_mask is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        # pdb.set_trace()
        if os.path.exists(self.results_path) is False:
                os.mkdir(str(self.results_path))
        self.results_list = []
        if fixed_image is None:
            fixed_image = self.fixed_image.split('\\')[-1]
            fixed_image = fixed_image[:-4]
            for moving_image in self.atlas_list:
                spec_results_path = os.path.join(self.results_path, 'atlas_img_' + moving_image + '_fixed_'+ fixed_image)
                self.results_list.append(spec_results_path)
                # path_moving_im = self.atlas_full_paths 


                full_path_moving_im = [i for i in self.atlas_full_paths if moving_image in i]
                pdb.set_trace()
                # 
                if os.path.exists(spec_results_path) is False:
                    os.mkdir(str(spec_results_path))
                print('moving image: \t' + moving_image)

                # pdb.set_trace()
                el = elastix.ElastixInterface(elastix_path=self.elastix_path)
                el.register(
                    fixed_image=self.fixed_image,
                    fixed_mask=self.fixed_im_mask,
                    moving_image=full_path_moving_im[0],
                    parameters=self.parameter_files,
                    output_dir=spec_results_path)
                
                # # transformix
                # transform_path = os.path.join(spec_results_path, 'TransformParameters.0.txt')
                
                # tr_output_dir = os.path.join(spec_results_path, 'transformix_results')
                # if os.path.exists(tr_output_dir) is False:
                #     os.mkdir(str(tr_output_dir))

                # tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=self.transformix_path)
                # tr.transform_image(image_path = os.path.join(spec_results_path, 'result.0.mhd'), output_dir=tr_output_dir)

        elif isinstance(fixed_image, str):
                spec_results_path = os.path.join(self.results_path, 'atlas_img_' + moving_image[:-4] + '_fixed_' + fixed_image[:-4])
                self.results_list.append(spec_results_path)
                # path_moving_im = self.atlas_full_paths 
                pdb.set_trace()
                full_path_moving_im = os.path.join(image_path, moving_image[:-4], moving_image) # wil not work for .nrrd files
                full_path_fixed_im = os.path.join(image_path, fixed_image[:-4], fixed_image)
                # pdb.set_trace()
                if os.path.exists(spec_results_path) is False:
                    os.mkdir(str(spec_results_path))

                print('moving image: \t' + moving_image)
                # pdb.set_trace()
                # affine transform
                el = elastix.ElastixInterface(elastix_path=self.elastix_path)
                el.register(
                    fixed_image=full_path_fixed_im,
                    fixed_mask=fixed_im_mask,
                    moving_image=full_path_moving_im,
                    parameters=self.parameter_files,
                    output_dir=spec_results_path)
                
                # # transformix
                # transform_path = os.path.join(spec_results_path, 'TransformParameters.0.txt')
                
                # tr_output_dir = os.path.join(spec_results_path, 'transformix_results')
                # if os.path.exists(tr_output_dir) is False:
                #     os.mkdir(str(tr_output_dir))

                # tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=self.transformix_path)
                # tr.transform_image(image_path = os.path.join(spec_results_path, 'result.0.mhd'), output_dir=tr_output_dir)
        else:
            print('Elastix was not used, check the input variable or for bugs in the code')
        



    # def bspline_elastix(self, affine_output_dirs = False):
    #     if self.atlas_dir is None:
    #         return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
    #     elif self.bspline_parameter_file is None:
    #         return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
    #     elif self.fixed_image is None:
    #         return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
    #     # elif self.fixed_im_mask is None:
    #     #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        

    #     # pdb.set_trace()
    #     for moving_image in self.atlas_list:
    #         spec_results_path = os.path.join(self.results_path, 'bspline_atlas_img_' + moving_image + '_fixed_'+ fixed_image[-10:-4])
    #         # path_moving_im = self.atlas_full_paths 
    #         # pdb.set_trace()
    #         if affine_output_dirs is not False:
    #             full_path_moving_im = [i for i in affine_output_dirs if moving_image in i]
    #             print('Bspline is performed on manually entered directories transformation done') 
    #         elif affine_output_dirs is False:
    #             full_path_moving_im = os.path.join(self.results_path, 'affine_atlas_img_' + moving_image + '_fixed_'+ fixed_image[-10:-4], 'result.mhd')
    #             print('Bspline is performed on earlier done affine transformations')

    #         # pdb.set_trace()
    #         if os.path.exists(spec_results_path) is False:
    #             os.mkdir(str(spec_results_path))

    #         print('moving image: \t' + moving_image)
    #         # pdb.set_trace()
    #         # affine transform
    #         el = elastix.ElastixInterface(elastix_path=self.elastix_path)
    #         el.register(
    #             fixed_image=self.fixed_image,
    #             fixed_mask=self.fixed_im_mask,
    #             moving_image=full_path_moving_im,
    #             parameters=[self.affine_parameter_file],
    #             output_dir=spec_results_path)
            
    #         # pdb.set_trace()
    #         # transformix
    #         transform_path = os.path.join(spec_results_path, 'TransformParameters.0.txt')
            
    #         tr_output_dir = os.path.join(spec_results_path, 'transformix_results')
    #         if os.path.exists(tr_output_dir) is False:
    #             os.mkdir(str(tr_output_dir))

    #         tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=transformix_path)
    #         tr.transform_image(image_path = os.path.join(spec_results_path, 'result.0.mhd'), output_dir=tr_output_dir)


    def apply_transformation(self, transformation_file_dir, segmentation_img_dir, fixed_image=None, moving_image=None):
        # transformix
        # if registratons have been done in the same operation, self.results_list can be used, otherwise the path has to be specified
            for spec_results_path in os.listdir(transformation_file_dir):
                # pdb.set_trace()
                transform_path = os.path.join(transformation_file_dir, spec_results_path, 'TransformParameters.1.txt')
                
                tr_output_dir = os.path.join(transformation_file_dir, spec_results_path, 'transformix_results')
                if os.path.exists(tr_output_dir) is False:
                    os.mkdir(str(tr_output_dir))

                # pdb.set_trace()
                # make code indicating what knee tructure it is:
                knee_struct = spec_results_path.split("_",3)[-1].split("_",4)  
                # pdb.set_trace()
            
                tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=self.transformix_path)
                tr.transform_image(image_path = os.path.join(segmentation_img_dir, 'result' +  + '.mhd'), output_dir=tr_output_dir)

    def show_evaluation(self):

        return None

if __name__ == "__main__":
    atlas_inputs = ['17_2016', '07_2017', '30_2017']
    a = Atlas(inputs = atlas_inputs)

    elastix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\elastix.exe')
    transformix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\transformix.exe')
    affine_parameter_file = r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\cadaver_knee_study2\code\elastix_parameter_files\parameters_similarity.txt'
    bspline_parameter_file = r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\cadaver_knee_study2\code\elastix_parameter_files\Parameters_BSpline_adjusted.txt'
    fixed_image = r"D:\masked_scans_bone\12_2018_femur\12_2018_femur.mhd"
    # fixed_mask = r'D:\segmentations PCCT Tim\masks\01_2019.nrrd' # FILL IN PATH TO .nrrd FILE
    atlas_path = r"D:\masked_scans_bone\17_2016_femur"
    results_path = r'D:\atlas_registration_results_test_bone_sim_Bspline'
    a.initialize_elastix(elastix_path, transformix_path, 
                         parameter_files=[affine_parameter_file, bspline_parameter_file], 
                         fixed_image=fixed_image, atlas_path=atlas_path, 
                         fixed_im_mask=None, results_path=results_path,
                         anatomical_structure='femur')
    # a.run_elastix(fixed_image='12_2018_femur.mhd', moving_image='17_2016_femur.mhd', image_path=r'D:\masked_scans_bone')
    a.run_elastix()
    # a.apply_transformation(segmentation_img_dir=r"D:\segmentations PCCT Tim\01_2019\01_2019.nrrd",
    #                        transformation_file_dir=r'D:\atlas_registration_results_test_bone_sim_Bspline')
    # a.bspline_elastix()

