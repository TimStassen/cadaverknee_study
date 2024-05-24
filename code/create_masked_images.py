import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb

im_path = r'E:\ME_data_mhd'
root_im_dir = os.listdir(im_path)

mask_path = r'E:\segmentations PCCT Tim\masks_flip'
root_mask_dir = os.listdir(mask_path)

output_path = r'E:\masked_scans'
if os.path.exists(output_path) is False:
    os.mkdir(str(output_path))

# mhd_path = r'E:\ME_data_mhd\01_2019\01_2019.mhd'


# mask_path = r'E:\segmentations PCCT Tim\masks_flip\01_2019.mhd'

for image, mask in zip(root_im_dir, root_mask_dir):
    new_scan_path = os.path.join(output_path, image)
    if os.path.exists(new_scan_path) is False:
        os.mkdir(str(new_scan_path))

    single_im_path = os.path.join(im_path, image, image + '.mhd')
    itk_image = sitk.ReadImage(single_im_path)
    image_array = sitk.GetArrayViewFromImage(itk_image)

    single_mask_path = os.path.join(mask_path, image, image + '.mhd')
    itk_image_mask = sitk.ReadImage(single_mask_path)
    mask_array = sitk.GetArrayViewFromImage(itk_image_mask)

    combined = mask_array*image_array
    inv_mask = (1-mask_array)*-3000
    combined_tr = combined+inv_mask
    # pdb.set_trace()

    spacing = itk_image.GetSpacing()
    origin = itk_image.GetOrigin()

    new_sitk_img = sitk.GetImageFromArray(combined_tr, isVector=False)
    new_sitk_img.SetSpacing(spacing)
    new_sitk_img.SetOrigin(origin)
    sitk.WriteImage(new_sitk_img, os.path.join(output_path, image + ".mhd"))
    print('Flipped mask stored at:', os.path.join(output_path, image + ".mhd"))


# plt.figure()
# fig, ax = plt.subplots(1, 3, figsize=(20, 5))
# ax[0].imshow(image_array[:,:,250], cmap='gray')
# ax[1].imshow(mask_array[:,:,250], cmap='gray')
# ax[2].imshow(combined[:,:,250], cmap='gray')
# plt.show()