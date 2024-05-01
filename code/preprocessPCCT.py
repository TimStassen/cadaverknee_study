# build code that preprocesses the PCCT data

# remove surroundings
# merge into one 3D array/tensor
# prepare to elastix readible format. 

import os
import SimpleITK as sitk
import numpy as np

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

    return  np.array(volume_list)
    