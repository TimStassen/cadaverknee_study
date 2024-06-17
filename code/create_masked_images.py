import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb
pdb.set_trace()
im_path = r'D:\cadaver_knee_study\data\MR\tijdspunt 2\240216_CADAVERKNEE_10.30_2017\dess'
root_im_dir = os.listdir(im_path)

mask_path = r'D:\30_2017_FOV_femur.nrrd'
root_mask_dir = os.listdir(mask_path)

output_path = r'D:\masked_scans_bone_MR'
if os.path.exists(output_path) is False:
    os.mkdir(str(output_path))
# # pdb.set_trace()
# full_path_ims = []
# for im in root_im_dir:
#     full_im_path = os.path.join(im_path, im)
#     full_path_ims.append(full_im_path)
# # pdb.set_trace()
reader = sitk.ImageSeriesReader()
dicom_names = reader.GetGDCMSeriesFileNames(im_path)
reader.SetFileNames(dicom_names)
itk_image = reader.Execute()
# itk_image = sitk.ReadImage(single_im_path)
image_array = sitk.GetArrayViewFromImage(itk_image)
# pdb.set_trace()

for mask in (root_mask_dir):
    # pdb.set_trace()
    new_scan_path = os.path.join(output_path, mask[-5])
    if os.path.exists(new_scan_path) is False:
        os.mkdir(str(new_scan_path))
    # mask_name_paths = mask.split('\\')[-1]
    # mask_name_paths = mask.split('_')
    
    single_mask_path = os.path.join(mask_path, mask[-5], mask)
    # pdb.set_trace()
    itk_image_mask = sitk.ReadImage(single_mask_path)
    mask_array = sitk.GetArrayViewFromImage(itk_image_mask)

    # mask_array = np.flip(mask_array, axis=0)

    combined = mask_array*image_array
    inv_mask = (1-mask_array)*-3000
    combined_tr = combined+inv_mask
    # pdb.set_trace()

    spacing = itk_image.GetSpacing()
    # pdb.set_trace()
    origin = itk_image.GetOrigin()

    new_sitk_img = sitk.GetImageFromArray(combined_tr, isVector=False)
    new_sitk_img.SetSpacing(spacing)
    new_sitk_img.SetOrigin(origin)
    sitk.WriteImage(new_sitk_img, os.path.join(output_path, mask[-5], mask[:-5]  + ".mhd"))
    print('Mask stored at:', os.path.join(output_path, mask[-5], mask[:-5]  + ".mhd"))
    # pdb.set_trace()


# mask needs to be flipped!


# # mask_path = r'E:\segmentations PCCT Tim\masks_flip\01_2019.mhd'
# for image, mask_dir in zip(root_mask_dir, root_im_dir):
#     # pdb.set_trace()
#     mask_dir = os.path.join(mask_path,mask_dir)
#     # for img in image:
#     masks = os.listdir(mask_dir)
#     # pdb.set_trace()

#     single_im_path = os.path.join(im_path, image, image+ '.mhd')
#     itk_image = sitk.ReadImage(single_im_path)
#     image_array = sitk.GetArrayViewFromImage(itk_image)
#     # pdb.set_trace()
#     for mask in (masks):
#         # pdb.set_trace()
#         new_scan_path = os.path.join(output_path, image)
#         if os.path.exists(new_scan_path) is False:
#             os.mkdir(str(new_scan_path))
    
#         mask_name_paths = mask.split('_')
        
#         single_mask_path = os.path.join(mask_path, image, mask)
#         # pdb.set_trace()
#         itk_image_mask = sitk.ReadImage(single_mask_path)
#         mask_array = sitk.GetArrayViewFromImage(itk_image_mask)

#         mask_array = np.flip(mask_array, axis=0)

#         combined = mask_array*image_array
#         inv_mask = (1-mask_array)*-3000
#         combined_tr = combined+inv_mask

#         # plt.figure()
#         # fig, ax = plt.subplots(1, 3, figsize=(20, 5))
#         # ax[0].imshow(image_array[:,:,250], cmap='gray')
#         # ax[1].imshow(mask_array[:,:,250], cmap='gray')
#         # ax[2].imshow(combined_tr[:,:,250], cmap='gray')
#         # plt.show()
#         # pdb.set_trace()

#         spacing = itk_image.GetSpacing()
#         origin = itk_image.GetOrigin()

#         new_sitk_img = sitk.GetImageFromArray(combined_tr, isVector=False)
#         new_sitk_img.SetSpacing(spacing)
#         new_sitk_img.SetOrigin(origin)
#         sitk.WriteImage(new_sitk_img, os.path.join(output_path, image, mask[:-5]  + ".mhd"))
#         print('Flipped mask stored at:', os.path.join(output_path, image, mask[:-5]  + ".mhd"))
#         # pdb.set_trace()