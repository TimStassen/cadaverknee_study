#%%
import os
import SimpleITK as sitk
import numpy as np

import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt



fix_path = r"D:\registration_results_test2\18_2018_femur\result.0.mhd"
itk_image = sitk.ReadImage(fix_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)

mov_path = r"D:\cadaver_knee_study\data\MR\tijdspunt 1\7T MRI\240130_CADAVERKNEE_1_182018\dess"
reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(mov_path)
reader.SetFileNames(dicom_names)
itk_image = reader.Execute()
# itk_image = sitk.ReadImage(single_im_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image)
#%%
# or_mov_path = r'E:\ME_data_mhd_fl\17_2016\17_2016.mhd'
# itk_image = sitk.ReadImage(or_mov_path)
# image_array3 = sitk.GetArrayViewFromImage(itk_image)
# plt.figure()
fig, ax = plt.subplots(1, 2, figsize=(20, 5))
# ax.imshow(image_array1[:,:,250], cmap='gray')
ax[0].imshow(image_array1[:,:,250], cmap='gray')
ax[1].imshow(image_array2[:,:,250], cmap='gray')
plt.show()
# imgplot = plt.imshow(image_array1)

# %%
