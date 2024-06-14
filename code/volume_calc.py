import SimpleITK as sitk
import os
import pdb
import csv

rootfolder_MR = r'E:\segmentations MR Tim'
rootfolder_CT = r'E:\TUe_segmentations'

rootdir_MR = os.listdir(rootfolder_MR)
rootdir_CT = os.listdir(rootfolder_CT)

data = {}
# >>> data.setdefault('foo', []).append(42)
# >>> data
# {'foo': [42]}

for MR_folder, CT_folder in zip(rootdir_CT, rootdir_MR):
    # pdb.set_trace()

    masks_MR_list = os.listdir(os.path.join(rootfolder_MR, MR_folder))
    masks_CT_list = os.listdir(os.path.join(rootfolder_CT, CT_folder))
    for MR_mask, CT_mask in zip(masks_MR_list, masks_CT_list):
        
        MR_scan_full_path = os.path.join(rootfolder_MR, MR_folder, MR_mask)
        CT_scan_full_path = os.path.join(rootfolder_CT, CT_folder, CT_mask)
        # pdb.set_trace()
        MR_name = MR_scan_full_path.split('.')[0]
        MR_name = MR_name.split('\\')[-1]
        MR_name = MR_name + '_MR'

        CT_name = CT_scan_full_path.split('.')[0]
        CT_name = CT_name.split('\\')[-1]
        CT_name = CT_name + '_CT'

        mr = sitk.ReadImage(MR_scan_full_path)
        shape_stats = sitk.LabelShapeStatisticsImageFilter()
        shape_stats.Execute(mr)
        MR_volume = shape_stats.GetPhysicalSize(1)
        data.setdefault(MR_name,[]).append(MR_volume)

        ct = sitk.ReadImage(CT_scan_full_path)
        shape_stats = sitk.LabelShapeStatisticsImageFilter()
        shape_stats.Execute(ct)
        CT_volume = shape_stats.GetPhysicalSize(1)
        data.setdefault(CT_name,[]).append(CT_volume)        
        # pdb.set_trace()

with open(r'E:\cartilage_volumes2.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in data.items():
       writer.writerow([key, value])


