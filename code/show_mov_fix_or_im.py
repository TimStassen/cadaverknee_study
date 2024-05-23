import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

fix_path = r'E:\ME_data_mhd_fl\08_2017R\08_2017R.mhd'
itk_image = sitk.ReadImage(fix_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)

mov_path = r'E:\atlas_registration_results_trial2\affine_atlas_img_17_2016_fixed__2017R\result.0.mhd'
itk_image = sitk.ReadImage(mov_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image)

or_mov_path = r'E:\ME_data_mhd_fl\17_2016\17_2016.mhd'
itk_image = sitk.ReadImage(or_mov_path)
image_array3 = sitk.GetArrayViewFromImage(itk_image)

fig, ax = plt.subplots(1, 3, figsize=(20, 5))
ax[0].imshow(image_array1[:,:,250], cmap='gray')
ax[1].imshow(image_array2[:,:,250], cmap='gray')
ax[1].imshow(image_array3[:,:,250], cmap='gray')
plt.show()