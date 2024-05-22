import os
import utils
import pdb

root_dir = r'D:\ME_data'
root_dir_list = os.listdir(root_dir)
root_output_dir = r'D:\ME_data_mhd'


for dir in root_dir_list:
    # files =  os.listdir(os.path.join(root_dir,dir))
    # for files
    dir_path = os.path.join(root_dir, dir)
    output_path = os.path.join(root_output_dir, str(dir), str(dir))
    # pdb.set_trace()
    utils.dcm2mhd(dir_path,output_path)
    print('Scan', dir, 'is converted to .mhd')

print('All DICOM directories converted to .mhd files')
