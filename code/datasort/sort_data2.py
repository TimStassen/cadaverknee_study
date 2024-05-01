# set up paths and folders
import shutil
import os
import pdb
import pydicom


# r is for a raw string (prevents escape sequence errors)
root_folder_path = r"C:\Users\T2025\Desktop\cadaver_knee_study\data\PCCT\sessie 2_16-02-2024"
knee_folders = os.listdir(root_folder_path)

# sort files
for k in knee_folders:

    # pdb.set_trace()
    knee_dir = os.listdir(os.path.join(root_folder_path, k))
    only_files = [ f for f in knee_dir if os.path.isfile(os.path.join(root_folder_path, k, f))]
    # count = 0
    for dcm in only_files:
        # pdb.set_trace()
        file = pydicom.dcmread(os.path.join(os.path.join(root_folder_path, k, dcm)))
        file_info = file[0x0008, 0x103e]
        file_info.value
        if all(s in file_info.value for s in ["12_2018", "0,20", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path,r"6. 12_2018\bone_0.2_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))


## tested above
        elif all(s in file_info.value for s in ["12_2018", "0,20", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path,r"6. 12_2018\bone_0.2_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        # elif all(s in file_info.value for s in ["12_2018", "0,20", "Br80"]):
        #     new_data_folder_path = os.path.join(root_folder_path, k,r"6. 12_2018\bone_0.2_Br80")
        #     shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["12_2018", "0,40", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\bone_0.4_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["12_2018", "0,40", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\bone_0.4_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["12_2018", "0,40", "Br80"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\bone_0.4_Br80")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["12_2018", "0,20", "Br44"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\soft_0.2_Br44")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))
        elif all(s in file_info.value for s in ["12_2018", "0,20", "Br48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\soft_0.2_Br48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["12_2018", "0,40", "Qr48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"6. 12_2018\0.4_Qr48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))
# 29_2017

        elif all(s in file_info.value for s in ["29_2017", "0,20", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\bone_0.2_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,20", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\bone_0.2_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        # elif all(s in file_info.value for s in ["29_2017", "0,20", "Br80"]):
        #     new_data_folder_path = os.path.join(root_folder_path, k,r"7. 29_2017\bone_0.2_Br80")
        #     shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,40", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\bone_0.4_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,40", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\bone_0.4_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,40", "Br80"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\bone_0.4_Br80")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,20", "Br44"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\soft_0.2_Br44")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,20", "Br48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\soft_0.2_Br48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["29_2017", "0,40", "Qr40"]):
            new_data_folder_path = os.path.join(root_folder_path, r"7. 29_2017\0.4_Qr40")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))
# 17_2016

        elif all(s in file_info.value for s in ["17_2016", "0,20", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\bone_0.2_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,20", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\bone_0.2_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        # elif all(s in file_info.value for s in ["17_2016", "0,20", "Br80"]):
        #     new_data_folder_path = os.path.join(root_folder_path, k,r"8. 17_2016\bone_0.2_Br80")
        #     shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,40", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\bone_0.4_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,40", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\bone_0.4_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,40", "Br80"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\bone_0.4_Br80")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,20", "Br44"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\soft_0.2_Br44")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,20", "Br48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\soft_0.2_Br48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["17_2016", "0,40", "Qr40"]):
            new_data_folder_path = os.path.join(root_folder_path, r"8. 17_2016\0.4_Qr40")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))
# 7_2017


        elif all(s in file_info.value for s in ["7_2017", "0,20", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\bone_0.2_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,20", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\bone_0.2_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        # elif all(s in file_info.value for s in ["7_2017", "0,20", "Br80"]):
        #     new_data_folder_path = os.path.join(root_folder_path, k,r"9. 7_2017\bone_0.2_Br80")
        #     shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,40", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\bone_0.4_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,40", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\bone_0.4_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,40", "Br80"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\bone_0.4_Br80")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,20", "Br44"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\soft_0.2_Br44")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,20", "Br48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\soft_0.2_Br48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["7_2017", "0,40", "Qr40"]):
            new_data_folder_path = os.path.join(root_folder_path, r"9. 7_2017\0.4_Qr40")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))
# 30_2017
        

        elif all(s in file_info.value for s in ["30_2017", "0,20", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\bone_0.2_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,20", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\bone_0.2_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        # elif all(s in file_info.value for s in ["30_2017", "0,20", "Br80"]):
        #     new_data_folder_path = os.path.join(root_folder_path, k,r"9. 30_2017\bone_0.2_Br80")
        #     shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,40", "Br68"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\bone_0.4_Br68")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,40", "Br72"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\bone_0.4_Br72")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,40", "Br80"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\bone_0.4_Br80")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,20", "Br44"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\soft_0.2_Br44")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,20", "Br48"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\soft_0.2_Br48")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))

        elif all(s in file_info.value for s in ["30_2017", "0,40", "Qr40"]):
            new_data_folder_path = os.path.join(root_folder_path, r"10. 30_2017\0.4_Qr40")
            shutil.copy2(os.path.join(root_folder_path, k, dcm), os.path.join(new_data_folder_path,dcm))


