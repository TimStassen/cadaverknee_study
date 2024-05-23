import os
import utils
import pdb

root_dir = r'E:\ME_data'
root_dir_list = os.listdir(root_dir)
root_output_dir = r'E:\ME_data_mhd_fl'

for dir in root_dir_list:
    dir_path = os.path.join(root_dir, dir)
    # pdb.set_trace()
    output_path = os.path.join(root_output_dir, str(dir))
    utils.dcm2mhd(dir_path,output_path,str(dir))
    print(f'Scan', dir, 'is converted to :', output_path)
    # pdb.set_trace()
print('All DICOM directories converted to .mhd' )