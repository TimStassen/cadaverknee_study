import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from scrollview import ScrollView
import pdb



fix_path = r'E:\atlas_registration_results_trial10_premask\affine_atlas_img_30_2017_fixed_01_2019\transformix_results\result.mhd'
itk_image = sitk.ReadImage(fix_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)
# pdb.set_trace()
image_array1_tr = np.einsum('kli->ikl', image_array1)

or_path = r'E:\ME_data_mhd\01_2019\01_2019.mhd'
itk_image2 = sitk.ReadImage(or_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image2)

image_array2_tr = np.einsum('kli->ikl', image_array2)


fig, ax = plt.subplots()
ScrollView(image_array1_tr).plot(ax, cmap='bone')
plt.show()

# fig, ax = plt.subplots()
# ScrollView(image_array2_tr).plot(ax, cmap='bone')
# plt.show()

# fig, ax = plt.subplots(1, 2, figsize=(20, 5))
# ax[0].imshow(image_array1[:,:,250], cmap='gray')
# ax[1].imshow(image_array2[:,:,250], cmap='gray')
# plt.show()