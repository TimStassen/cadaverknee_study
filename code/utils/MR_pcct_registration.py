""" 
This file is created for the semi-automatic registration approach 
as part of a project done at the Orthopeadic Surgery department of Maastricht University. 
This work is done in the fullfillment of the MSc Biomedical Engineering internship 
in the  Medical Image Analysis group at the TU/e (course code: 8ZM05)


This utils code file contains the objects and functions
supporting the analysis of the PCCT and MR segmetation similarity

by Tim Stassen (student number: 1633023) 
"""

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
    """ Image registration class.
        Initializes and runs elastix with all the required information
    """
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
        """ add the relevant anatomical structures to the indices of the directory list (dirlist)
        i.e. 'femur', 'tibia', 'patella'
        Parameter(s):   path:                (str)  The path of the atlas directory, if 
                                                    'None' self.path during initialization is used.
        Returns:                             (list) The directory list containing full paths of the knee scans     
            """
        full_paths = []
        for scan in self.atlas_list:
             
            # atlas_full_paths.append(os.path.join(self.path, scan, scan +'.mhd'))
                 
            for anatomical_struct in ['_femur', '_tibia', '_patella']:
                full_paths.append(os.path.join(self.path, scan, scan + anatomical_struct +'.mhd'))

        if 'femur' in self.fixed_image:
            full_paths_filt = [e for e in full_paths if "femur" in e]
        elif 'tibia' in self.fixed_image:
            full_paths_filt = [e for e in full_paths if "tibia" in e]
        elif 'patella' in self.fixed_image:
            full_paths_filt = [e for e in full_paths if "patella" in e]
        # elif 'fibula' in self.fixed_image:
        #     atlas_full_paths_filt = [e for e in atlas_full_paths if "fibula" in e]
        self.atlas_full_paths = full_paths_filt
        return full_paths

    
    def initialize_elastix(self, elastix_path, transformix_path, parameter_files, fixed_image,
                            moving_image, fixed_im_mask, results_path, anatomical_structure=None):
        """ Initialize the object to perform the registration
            Parameter(s):   elastix_path:                   (str)   Path to the elastix executable (.exe) file
                            transformix_path:               (str)   Path to the transformix executable (.exe) file
                            parameter_files:                (str)   Path to the elastix parameter files
                            fixed_image:                    (str)   Path to the fixed input image 
                            atlas_path:                     (list)  List containing the paths to the atlas (moving) files
                            fixed_im_mask:                  (str)   path to fixed image mask file 
                            results_path:                   (str)   Path where results will be stored 
                            anatomical_structure:
            Returns:        
                """
        
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
        """ Initialize the object to perform the registration
            Parameter(s):   fixed_image:                    (str)   Path to the fixed input image 
                            fixed_im_mask:                  (str)   path to fixed image mask file 
                            image_path:                     (str)   Path path (without filename) of moving and fixed image 
                            anatomical_structure:
            Returns:        
        """
        if os.path.exists(self.results_path) is False:
                os.mkdir(str(self.results_path))
        self.results_list = []
        if fixed_image is None:
            fixed_image = self.fixed_image.split('\\')[-1]
            fixed_image = fixed_image[:-4]
            moving_image = self.moving_image.split('\\')[-1]
            moving_image = moving_image[:-4]

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
                    

        else:
            print('Elastix was not used, check the input variable or for bugs in the code')
        


    def apply_transformation(self, transformation_file_dir, segmentation_img, fixed_image=None, moving_image=None, transformix_path=None):
        """ Initialize the object to perform the registration
            Parameter(s):   transformation_file_dir:        (str)   Path to transformation results dir
                            segmentation_img:               (str)   path to the segmentation mask file
                            fixed_image:                    (str)   Path to the fixed input image 
                            moving_image:                   (str)   path to fixed image mask file 
                            image_path:                     (str)   Path path (without filename) of moving and fixed image 
                            transformix_path:               (str)   Path to the transformix executable (.exe) file
            Returns:        
        """
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
    
        tr = elastix.TransformixInterface(parameters=transform_file1, transformix_path=transformix_path)
        tr.transform_image(image_path = segmentation_img, output_dir=tr_output_dir1)

if __name__ == "__main__":
    # atlas_inputs = ['17_2016', '07_2017', '30_2017']
    a = Image_Registration()

    elastix_path = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
    transformix_path = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')
    affine_parameter_file = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\elastix_parameter_files\parameters_MR_pcct.txt'
    # fixed_image = r'E:\MR_bone_segs\07_2017\07_2017_femur.nrrd' #MR
    # fixed_mask = r'D:\segmentations PCCT Tim\masks\01_2019.nrrd' # FILL IN PATH TO .nrrd FILE
    fixed_image = r'E:\TUe_masked_MR\30_2017\30_2017_tibia.nrrd' #MR
    moving_image = r"E:\segmentations PCCT Tim\bone_segs\nrrd\30_2017\30_2017_tibia.nrrd" #PCCT
    # moving_image = r"D:\ME_data_mhd\07_2017\07_2017.mhd" #PCCT
    results_path = r'E:\registration_results_test22'


    a.initialize_elastix(elastix_path, transformix_path, 
                         parameter_files=[affine_parameter_file], 
                         fixed_image=fixed_image, moving_image=moving_image, 
                         fixed_im_mask=None, results_path=results_path,
                        #  anatomical_structure='femur'
                         )
    # a.run_elastix(fixed_image='12_2018_femur.mhd', moving_image='17_2016_femur.mhd', image_path=r'D:\masked_scans_bone')
    a.run_elastix()


    segmentation_path = r'E:\TUe_segmentations_PCCT\30_2017' # PCCT
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
        seg_img =os.path.join(segmentation_path, seg_img_name + cartilage + '.nrrd') # or nrrd if it is not converted
        # transform_matrix0 = os.path.join(registrations_dir_path, registration, 'TransformParameters.0.txt')
        transformation_file_dir = os.path.join(results_path, registration)
        # pdb.set_trace()   
        # a.initialize_elastix(elastix_path, transformix_path, affine_parameter_file=affine_parameter_file, 
        #                         bspline_parameter_file=bspline_parameter_file,
        #                         fixed_image=fixed_image, atlas_path=atlas_path, 
        #                         fixed_im_mask=fixed_mask, results_path=results_path)
        
        a.apply_transformation(transformation_file_dir, seg_img, fixed_image=None, moving_image=None, transformix_path=transformix_path)