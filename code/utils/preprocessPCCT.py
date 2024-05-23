# build code that preprocesses the PCCT data

# remove surroundings
# merge into one 3D array/tensor
# prepare to elastix readible format. 

import os
import SimpleITK as sitk
import numpy as np
import glob
import pydicom
import pdb

def order_by_slice_location(slice):
    return float(slice.GetMetaData('0020|1041'))


def create3D_input(path):
    dicom_filenames = os.listdir(path)

    # only include the non-constrast images
    list_of_slices = []
    for filename in dicom_filenames:
        dicom_path = os.path.join(path, filename)
        slice = sitk.ReadImage(dicom_path)
        if 'Monoenergetic Plus Knee Noncon' in slice.GetMetaData('0008|103e'):
            list_of_slices.append(slice)
    PixelSpacing = slice.GetMetaData('0028|0030').split("\\")
    Spacing = (float(PixelSpacing[0]), float(PixelSpacing[1]), float(slice.GetMetaData('0018|0050')))
    Origins = slice.GetMetaData('0020|0032').split("\\")
    Origin = (float(Origins[0]), float(Origins[1]), float(Origins[2]))

    list_of_slices.sort(key=order_by_slice_location, reverse=True)

    volume_list = []
    for slice in list_of_slices:
        volume_list.append(sitk.GetArrayViewFromImage(slice)[0])

    return  {'im_array': np.array(volume_list), 'Spacing': Spacing, 'Origin': Origin}
    

# def dcm2mhd_old(input_dir, output_dir, new_filename):
   
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir) 

#     dcm_dir = glob.glob(input_dir)
#     dcm_dir_list = os.listdir(dcm_dir[0])
#     image = pydicom.read_file(dcm_dir_list[0])
#     dim = (int(image.Rows), int(image.Columns), len(dcm_dir))
#     spacing = (float(image.PixelSpacing[0]), float(image.PixelSpacing[1]), float(image.SliceThickness))
#     origin = image.ImagePositionPatient
#     NpArrDc = np.zeros(dim, dtype=image.pixel_array.dtype)
#     for filename in dcm_dir_list:
#         df = pydicom.read_file(filename)
#         NpArrDc[:,:,dcm_dir.index(filename)] = df.pixel_array

#     # NpArrDc = np.transpose(NpArrDc, (2,0,1))
#     sitk_img = sitk.GetImageFromArray(NpArrDc, isVector=False)
#     sitk_img.SetSpacing(spacing)
#     sitk_img.SetOrigin(origin)
#     sitk.WriteImage(sitk_img, os.path.join(output_dir, new_filename + ".mhd"))
#     print("converting .dcm to .mhd done and stored at: \n" + os.path.join(output_dir, new_filename + ".mhd"))

def dcm2mhd(input_dir, output_dir, new_filename):
   
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 

    dcm_dir = glob.glob(input_dir)
    # pdb.set_trace()
    dcm_dir_list = os.listdir(dcm_dir[0])
    image = pydicom.read_file(os.path.join(input_dir,dcm_dir_list[0]))
    dim = (int(image.Rows), int(image.Columns), len(dcm_dir))
    spacing = (float(image.PixelSpacing[0]), float(image.PixelSpacing[1]), float(image.SliceThickness))
    origin = image.ImagePositionPatient
    im_array = create3D_input(input_dir)
    # pdb.set_trace()
    im_array_arr = np.flip(im_array['im_array'], axis=0)
    
    # pdb.set_trace()
    sitk_img = sitk.GetImageFromArray(im_array_arr, isVector=False)
    sitk_img.SetSpacing(spacing)
    sitk_img.SetOrigin(origin)
    sitk.WriteImage(sitk_img, os.path.join(output_dir, new_filename + ".mhd"))
    print("converting .dcm to .mhd done and stored at: \n" + os.path.join(output_dir, new_filename + ".mhd"))
    