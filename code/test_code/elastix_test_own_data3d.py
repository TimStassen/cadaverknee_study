#%%

from __future__ import print_function, absolute_import
import elastix
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
import elastix
import utils
#%%

# root_folder = r'C:\Users\T2025\Desktop\cadaver_knee_study\data\PCCT'
# data_path = r'C:\Users\T2025\Desktop\cadaver_knee_study\data\PCCT\ME_data\07_2017'



#%%
# IMPORTANT: these paths may differ on your system, depending on where
# Elastix has been installed. Please set accordingly.
ELASTIX_PATH = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\elastix.exe')
TRANSFORMIX_PATH = os.path.join(r'C:\Users\20201900\Desktop\Master BME\8DM20\elastix\transformix.exe')

if not os.path.exists(ELASTIX_PATH):
    raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
if not os.path.exists(TRANSFORMIX_PATH):
    raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

# Make a results directory if non exists
if os.path.exists('results_own_data') is False:
    os.mkdir('results_own_data')

# moving_image_path = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\test_code\moving_im.jpg'
# fixed_image_path = r'C:\Users\T2025\Desktop\cadaver_knee_study\code\test_code\fixed_im.jpg'

# fixed_image = utils.create3D_input(r'D:\ME_data\07_2017')
# moving_image = utils.create3D_input(r'D:\ME_data\01_2019')

# fixed_image = os.listdir(r'D:\test_fix')
# moving_image = os.listdir(r'D:\test_mov')

# fixed_images = os.listdir(r'D:\test_fix')
# moving_images = os.listdir(r'D:\test_mov')

# full_fixed_im_path = []
# for file in fixed_images:
#     full_path = os.path.join(r'D:\test_fix',file)
#     full_fixed_im_path.append(full_path)

# full_moving_im_path = []
# for file in moving_images:
#     full_path = os.path.join(r'D:\test_mov',file)
#     full_moving_im_path.append(full_path)

# max_len_scan = np.min([len(full_fixed_im_path), len(full_moving_im_path)])


full_fixed_im = r'C:\Users\20201900\Desktop\Master BME\8DM20\ProcessedData\128\128_mr_bffe.mhd'
full_moving_im = r'C:\Users\20201900\Desktop\Master BME\8DM20\ProcessedData\108\108_mr_bffe.mhd'

# full_fixed_im = r'C:\Users\20201900\Desktop\knees\07_2017\07_2017.mhd'
# full_moving_im = r'C:\Users\20201900\Desktop\knees\01_2019\01_2019.mhd'


#%%
el = elastix.ElastixInterface(elastix_path=ELASTIX_PATH)
el.register(
    fixed_image=full_fixed_im,
    moving_image=full_moving_im,
    parameters=[r'C:\Users\20201900\Desktop\cadaver_knee_study2-main\code\test_code\elastix\\parameters_affine.txt'], # parameters_bspline_multires_MR.txt
    output_dir='results_own_data')

# result_path = os.path.join(root_folder,'results', 'result.0.tiff')

# Find the results
transform_path = os.path.join('results_own_data', 'TransformParameters.0.txt')
result_path = os.path.join('results_own_data', 'result.0.nii')
#%%
# Open the logfile into the dictionary log
for i in range(3):
    log_path = os.path.join('results_own_data', 'IterationInfo.0.R{}.txt'.format(i))
    log = elastix.logfile(log_path)
    # Plot the 'metric' against the iteration number 'itnr'
    plt.plot(log['itnr'], log['metric'])
plt.legend(['Resolution {}'.format(i) for i in range(5)])

# # Load the fixed, moving, and result images
fixed_image = imageio.v2.imread(full_fixed_im)[50, :, :]
moving_image = imageio.v2.imread(full_moving_im)[50, :, :]
transformed_moving_image = imageio.v2.imread(result_path)[50,:,:]

# Show the resulting image side by side with the fixed and moving image
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
ax[0].imshow(fixed_image, cmap='gray')
ax[0].set_title('Fixed image')
ax[1].imshow(moving_image, cmap='gray')
ax[1].set_title('Moving image')
ax[2].imshow(transformed_moving_image, cmap='gray')
ax[2].set_title('Transformed\nmoving image')

# %%
