import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

mhd_path = r'E:\ME_data_mhd\08_2017\08_2017.mhd'
itk_image = sitk.ReadImage(mhd_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)

nrrd_path = r'E:\segmentations PCCT Tim\masks\08_2017.nrrd'
itk_image = sitk.ReadImage(nrrd_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image)

fig, ax = plt.subplots(1, 2, figsize=(20, 5))
ax[0].imshow(image_array1[:,:,250], cmap='gray')
# ax[1].imshow(image_array2[:,:,250], cmap='gray')
plt.show()