from __future__ import print_function, absolute_import

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
        self.parameter_file = None
        self.fixed_image = None
        self.fixed_im_mask = None
        self.affine_parameter_file = None
        self.bspline_parameter_file = None


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
        
        # if scan in all_scan_codes for scan in all_scan_codes.inputs:
    def create_atlas_dir(self, path=None):
        if path is None and self.path is None:
            return f"Variable: 'path', is not defined"
        elif path is None:
            path = self.path
        elif self.path is None:
            self.path = path

        self.atlas_list = self._check_atlas_codes()

        atlas_full_paths = []
        for scan in self.atlas_list:
            atlas_full_paths.append(os.path.join(self.path, scan, scan+'.mhd'))
        self.atlas_full_paths = atlas_full_paths
        
        return self.atlas_full_paths
    
    def initialize_elastix(self, elastix_path, transformix_path, affine_parameter_file, bspline_parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path):
        
        self.elastix_path = elastix_path
        self.transformix_path = transformix_path

        if not os.path.exists(self.elastix_path):
            raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
        if not os.path.exists(self.transformix_path):
            raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

        self.atlas_dir = self.create_atlas_dir(atlas_path)
        self.affine_parameter_file = affine_parameter_file
        self.bspline_parameter_file = bspline_parameter_file
        self.fixed_image = fixed_image
        self.fixed_im_mask = fixed_im_mask
        self.results_path = results_path
        # pdb.set_trace()
        

    def affine_elastix(self):
        if self.atlas_dir is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        elif self.affine_parameter_file is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')         
        elif self.fixed_image is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        # elif self.fixed_im_mask is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        
        self.results_list = []
        for moving_image in self.atlas_list:
            spec_results_path = os.path.join(self.results_path, 'affine_atlas_img_' + moving_image + '_fixed_'+ fixed_image[-10:-4])
            self.results_list.append(spec_results_path)
            # path_moving_im = self.atlas_full_paths 

            full_path_moving_im = [i for i in self.atlas_full_paths if moving_image in i]

            # pdb.set_trace()
            if os.path.exists(spec_results_path) is False:
                os.mkdir(str(spec_results_path))

            print('moving image: \t' + moving_image)
            # pdb.set_trace()
            # affine transform
            el = elastix.ElastixInterface(elastix_path=self.elastix_path)
            el.register(
                fixed_image=self.fixed_image,
                moving_image=full_path_moving_im[0],
                parameters=[self.affine_parameter_file],
                output_dir=spec_results_path)
            
            # transformix
            transform_path = os.path.join(spec_results_path, 'TransformParameters.0.txt')
            
            tr_output_dir = os.path.join(spec_results_path, 'transformix_results')
            if os.path.exists(tr_output_dir) is False:
                os.mkdir(str(tr_output_dir))

            tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=transformix_path)
            tr.transform_image(image_path = os.path.join(spec_results_path, 'result.0.mhd'), output_dir=tr_output_dir)
        



    def bspline_elastix(self, affine_output_dirs = False):
        if self.atlas_dir is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        elif self.bspline_parameter_file is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        elif self.fixed_image is None:
            return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        # elif self.fixed_im_mask is None:
        #     return print('First initialize elastix properly. \n Initialize by a = Atlas(path=path) \n a.initialize_elastix(elastix_path, transformix_path, parameter_file, fixed_image, atlas_path, fixed_im_mask, results_path) \n a.run_elastix()')
        

        # pdb.set_trace()
        for moving_image in self.atlas_list:
            spec_results_path = os.path.join(self.results_path, 'bspline_atlas_img_' + moving_image + '_fixed_'+ fixed_image[-10:-4])
            # path_moving_im = self.atlas_full_paths 
            # pdb.set_trace()
            if affine_output_dirs is not False:
                full_path_moving_im = [i for i in affine_output_dirs if moving_image in i]
                print('Bspline is performed on manually entered directories transformation done') 
            elif affine_output_dirs is False:
                full_path_moving_im = os.path.join(self.results_path, 'affine_atlas_img_' + moving_image + '_fixed_'+ fixed_image[-10:-4], 'result.mhd')
                print('Bspline is performed on earlier done affine transformations')

            # pdb.set_trace()
            if os.path.exists(spec_results_path) is False:
                os.mkdir(str(spec_results_path))

            print('moving image: \t' + moving_image)
            # pdb.set_trace()
            # affine transform
            el = elastix.ElastixInterface(elastix_path=self.elastix_path)
            el.register(
                fixed_image=self.fixed_image,
                moving_image=full_path_moving_im,
                parameters=[self.affine_parameter_file],
                output_dir=spec_results_path)
            
            # pdb.set_trace()
            # transformix
            transform_path = os.path.join(spec_results_path, 'TransformParameters.0.txt')
            
            tr_output_dir = os.path.join(spec_results_path, 'transformix_results')
            if os.path.exists(tr_output_dir) is False:
                os.mkdir(str(tr_output_dir))

            tr = elastix.TransformixInterface(parameters=transform_path, transformix_path=transformix_path)
            tr.transform_image(image_path = os.path.join(spec_results_path, 'result.0.mhd'), output_dir=tr_output_dir)


    def show_evaluation(self):

        return None


if __name__ == "__main__":
    atlas_inputs = ['17_2016', '07_2017', '30_2017']
    a = Atlas(inputs = atlas_inputs)
    # a.create_atlas_dir(path=None) #r'D:\dcm2mhd'

    elastix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\elastix.exe')
    transformix_path = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\transformix.exe')
    affine_parameter_file = r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\test_code\elastix\\parameters_affine.txt'
    bspline_parameter_file = r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\test_code\elastix\parameters_bspline_multires.txt'
    fixed_image = r'D:\dcm2mhd\01_2019\01_2019.mhd'
    fixed_image_mask = r'D:\segmentations PCCT Tim\masks\01_2019.nrrd'
    atlas_path = r'D:\ME_data_mhd'
    results_path = r'D:\atlas_registration_results_trial1'
    a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
                         bspline_parameter_file=bspline_parameter_file,
                         fixed_image=fixed_image, atlas_path=atlas_path, 
                         fixed_im_mask=fixed_image_mask, results_path=results_path)
    a.affine_elastix()
    # a.bspline_elastix()
# %%
