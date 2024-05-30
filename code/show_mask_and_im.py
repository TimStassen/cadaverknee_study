import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

mhd_path = r'E:\ME_data_mhd\12_2018\12_2018.mhd'
itk_image = sitk.ReadImage(mhd_path)
image_array = sitk.GetArrayViewFromImage(itk_image)

mask_path = r'E:\segmentations PCCT Tim\bone_segs\nrrd\12_2018\flipped_correct\12_2018_femur.mhd'
itk_image_mask = sitk.ReadImage(mask_path)
mask_array = sitk.GetArrayViewFromImage(itk_image_mask)

combined = mask_array*image_array

plt.figure()
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
ax[0].imshow(image_array[:,:,250], cmap='gray')
ax[1].imshow(mask_array[:,:,250], cmap='gray')
ax[2].imshow(combined[:,:,250], cmap='gray')
plt.show()