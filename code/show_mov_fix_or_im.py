import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

fix_path = r'D:\ME_data_mhd\12_2018\12_2018.mhd'
itk_image = sitk.ReadImage(fix_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)

mov_path = r'D:\atlas_registration_results_test_bone\affine_atlas_img_17_2016_femur.mhd_fixed__femur\transformix_results\result.mhd'
itk_image = sitk.ReadImage(mov_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image)

# or_mov_path = r'E:\ME_data_mhd_fl\17_2016\17_2016.mhd'
# itk_image = sitk.ReadImage(or_mov_path)
# image_array3 = sitk.GetArrayViewFromImage(itk_image)
# plt.figure()
fig, ax = plt.subplots(1, 2, figsize=(20, 5))
ax[0].imshow(image_array1[:,:,250], cmap='gray')
ax[1].imshow(image_array2[:,:,250], cmap='gray')
# ax[1].imshow(image_array3[:,:,250], cmap='gray')
plt.show()
