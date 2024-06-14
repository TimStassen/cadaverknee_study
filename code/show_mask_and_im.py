import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb

import matplotlib            
print(matplotlib.rcParams['backend'])

# pdb.set_trace()

mhd_path = r'E:\ME_data_mhd\01_2019\01_2019.mhd'
itk_image = sitk.ReadImage(mhd_path)
image_array1 = sitk.GetArrayViewFromImage(itk_image)

nrrd_path = r'E:\atlas_registration_results_bone_segs\atlas_img_07_2017_fixed_01_2019_femur\transformix_results0\result.mhd'
itk_image = sitk.ReadImage(nrrd_path)
image_array2 = sitk.GetArrayViewFromImage(itk_image)

# pdb.set_trace()

plt.figure()
# fig, ax = plt.subplots(1, 2, figsize=(20, 5))
# ax[0].imshow(image_array1[:,:,250], cmap='gray')
# ax[1].imshow(image_array2[:,:,250], cmap='gray')
# fig.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
ax1.imshow(image_array1[:,:,250], cmap='gray')
ax2.imshow(image_array2[:,:,250], cmap='gray')
