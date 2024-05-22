# build code that preprocesses the PCCT data

# remove surroundings
# merge into one 3D array/tensor
# prepare to elastix readible format. 

import os
import SimpleITK as sitk
import numpy as np
import pydicom
import glob
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
        if 'Monoenergetic Plus Knee Noncontrast#0' in slice.GetMetaData('0008|103e'):
            list_of_slices.append(slice)

    list_of_slices.sort(key=order_by_slice_location, reverse=True)

    volume_list = []
    for slice in list_of_slices:
        volume_list.append(sitk.GetArrayViewFromImage(slice)[0])
    image_array = np.array(volume_list)
    
    return sitk.GetImageFromArray(image_array)


def dcm2mhd(input_path,output_path):
    '''
    Procedure:
    # To get first image as refenece image, supposed all images have same dimensions
    # To get Dimensions, 3D spacing, image origin
    # To make numpy array
    # loop through all the DICOM files
        # To read the dicom file
        # store the raw image data
    :param input_path: the path of dicom files
    :param output_path: the output path of mhd files
    :return: null
    '''
    DICOM_directory = os.listdir(input_path)
    # DICOM_directory = glob.glob(DICOM_directory)
    output_dir = output_path[:output_path.find('\\', -10, -1)]
    # pdb.set_trace()
    if os.path.exists(output_dir) is False:
        os.mkdir(str(output_dir))

    Image = pydicom.read_file(os.path.join(input_path,DICOM_directory[0]))
    Dimension = (int(Image.Rows), int(Image.Columns), len(DICOM_directory))
    # pdb.set_trace()
    Spacing = (float(Image.PixelSpacing[0]), float(Image.PixelSpacing[1]), float(Image.SliceThickness))
    Origin = Image.ImagePositionPatient
    NpArrDc = np.zeros(Dimension, dtype=Image.pixel_array.dtype)
    for filename in DICOM_directory:
        df = pydicom.read_file(os.path.join(input_path,filename))
        NpArrDc[:, :, DICOM_directory.index(filename)] = df.pixel_array

    NpArrDc = np.transpose(NpArrDc, (2, 0, 1))  # axis transpose
    sitk_img = sitk.GetImageFromArray(NpArrDc, isVector=False)
    sitk_img.SetSpacing(Spacing)
    sitk_img.SetOrigin(Origin)
    sitk.WriteImage(sitk_img, os.path.join(output_path + ".mhd"))
