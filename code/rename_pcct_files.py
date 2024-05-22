#%%
import SimpleITK as sitk
import os 

writer = sitk.ImageFileWriter()

dir = r'D:\test_mov'
new_dir = r'D:\test_mov_newname'
scan_code = '1_2019'

#%%
def order_by_slice_location(slice):
    return float(slice.GetMetaData('0020|1041'))
#%%

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

dicom_filenames = os.listdir(dir)

list_of_slices = []
for filename in dicom_filenames:
    dicom_path = os.path.join(dir, filename)
    slice = sitk.ReadImage(dicom_path)
    slice_nr = order_by_slice_location(slice)
    outputImageFileName = os.path.join(new_dir, scan_code + '_slice_' + str(slice_nr)+'.dcm')
    sitk.WriteImage(slice, outputImageFileName)

# %%
