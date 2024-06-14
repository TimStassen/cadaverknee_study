import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb

def flip_masks(mask_path, im_path, output_path):
    if os.path.exists(output_path) is False:
        os.mkdir(str(output_path))

    scan_name = mask_path.split('\\')[-1]
    scan_name = scan_name
    # pdb.set_trace()
    # nrrd_path = r'E:\segmentations PCCT Tim\masks\08_2017.nrrd'
    itk_mask = sitk.ReadImage(mask_path)
    image_array = sitk.GetArrayViewFromImage(itk_mask)
    # image_array2.shape
    
    image_array_fl = np.flip(image_array, axis=0)

    # get original image for metadata
    # offset and elementspacing
    itk_image = sitk.ReadImage(im_path)
    spacing = itk_image.GetSpacing()
    origin_ = itk_image.GetOrigin()
    origin = [origin_[0], origin_[1], 1479.389]
    origin = tuple(origin)
    pdb.set_trace()

    sitk_img = sitk.GetImageFromArray(image_array_fl, isVector=False)
    sitk_img.SetSpacing(spacing)
    sitk_img.SetOrigin(origin)
    sitk.WriteImage(sitk_img, os.path.join(output_path, scan_name))
    print('Flipped mask stored at:', os.path.join(output_path, scan_name))


if __name__ == "__main__":
    root_mask_path = r'E:\segmentations PCCT Tim\TUe\18_2018'
    root_mask_dir = os.listdir(root_mask_path)
    root_im_path = r'E:\ME_data_mhd'
    output_path = r'E:\segmentations PCCT Tim\TUe\18_2018_correct'
    for image in root_mask_dir:
        if image.split('.')[-1] == 'mhd':
            # pdb.set_trace()
            mask_path = os.path.join(root_mask_path, image)
            # mask_path = os.listdir(mask_path)
            im_path = os.path.join(root_im_path, image[:7], image[:7] + '.mhd')
            # pdb.set_trace()
            flip_masks(mask_path, im_path, output_path)
        elif image.split('.')[-1] == 'nrrd':
            mask_path = os.path.join(root_mask_path, image)
            im_path = os.path.join(root_im_path, image[:7], image[:7] + '.mhd')
            flip_masks(mask_path, im_path, output_path)
        elif image.split('.')[-1] == 'raw':
            continue

    # image = sitk.ReadImage(r'E:\ME_data_mhd\08_2017\08_2017.mhd', imageIO="MetaImageIO")
    # elementspacing = image.GetSpacing()
    # offset = image.GetOrigin()
    # pdb.set_trace()
    # image = reader.SetFileName(r'E:\ME_data_mhd\08_2017\08_2017.mhd')
    # for key in image.GetMetaDataKeys():
    #     print(image.GetMetaData(key))
    # # pdb.set_trace()
