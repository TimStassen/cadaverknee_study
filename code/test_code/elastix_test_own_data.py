from __future__ import print_function, absolute_import
import elastix
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
import elastix



# IMPORTANT: these paths may differ on your system, depending on where
# Elastix has been installed. Please set accordingly.
ELASTIX_PATH = os.path.join(r'C:\Tim\Software\Elastix\elastix.exe')
TRANSFORMIX_PATH = os.path.join(r'C:\Tim\Software\Elastix\transformix.exe')

if not os.path.exists(ELASTIX_PATH):
    raise IOError('Elastix cannot be found, please set the correct ELASTIX_PATH.')
if not os.path.exists(TRANSFORMIX_PATH):
    raise IOError('Transformix cannot be found, please set the correct TRANSFORMIX_PATH.')

# Make a results directory if non exists
if os.path.exists('results_own_data') is False:
    os.mkdir('results_own_data')

moving_image_path = r'E:\dcm2mhd\01_2019_2\01_2019_2.mhd'
fixed_image_path = r'E:\dcm2mhd\07_2017_2\07_2017_2.mhd'


el = elastix.ElastixInterface(elastix_path=ELASTIX_PATH)
el.register(
    fixed_image=fixed_image_path,
    moving_image=moving_image_path,
    parameters=[r'C:\Users\T2025\Desktop\cadaver_knee_study\code\test_code\elastix\parameters_bspline_multires_MR.txt'],
    output_dir='results_own_data')

# result_path = os.path.join(root_folder,'results', 'result.0.tiff')

# Find the results
transform_path = os.path.join('results_own_data', 'TransformParameters.0.txt')
result_path = os.path.join('results_own_data', 'result.0.tiff')

# Open the logfile into the dictionary log
for i in range(5):
    log_path = os.path.join('results_own_data', 'IterationInfo.0.R{}.txt'.format(i))
    log = elastix.logfile(log_path)
    # Plot the 'metric' against the iteration number 'itnr'
    plt.plot(log['itnr'], log['metric'])
plt.legend(['Resolution {}'.format(i) for i in range(5)])

# Load the fixed, moving, and result images
fixed_image = imageio.v2.imread(fixed_image_path)[:, :, 0]
moving_image = imageio.v2.imread(moving_image_path)[:, :, 0]
transformed_moving_image = imageio.v2.imread(result_path)

# Show the resulting image side by side with the fixed and moving image
fig, ax = plt.subplots(1, 4, figsize=(20, 5))
ax[0].imshow(fixed_image, cmap='gray')
ax[0].set_title('Fixed image')
ax[1].imshow(moving_image, cmap='gray')
ax[1].set_title('Moving image')
ax[2].imshow(transformed_moving_image, cmap='gray')
ax[2].set_title('Transformed\nmoving image')
