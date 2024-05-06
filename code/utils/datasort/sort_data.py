# Code to sort the PCCT DICOM files from the Siemens Naeotom Alpha to the correct folder.
# made for the data scanned in the first session

# set up paths and folders
import shutil
import os
import pdb


# r is for a raw string (prevents escape sequence errors)
data_folder_path = r"C:\Users\T2025\Desktop\cadaver_knee_study\data\PCCT\sessie 1_30-01-2024"
data = os.listdir(data_folder_path)
only_files = [ f for f in os.listdir(data_folder_path) if os.path.isfile(os.path.join(data_folder_path, f))]



# sort files
for f in only_files:
# earlier files and commented lines have already been sorted
    
# 10_2019
    # for testing
    # if "Schaedel_nach_C.CT.Knie(Adult).23" in f:
    #     pdb.set_trace()
    if "Schaedel_nach_C.CT.Knie(Adult).23" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"2. 01_2019\bone_0.4_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).24" in f:
        new_data_folder_path = os.path.join(data_folder_path,r"2. 01_2019\bone_0.4_Br80")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).25" in f:
        new_data_folder_path = os.path.join(data_folder_path,r"2. 01_2019\soft_0.2_Br44")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))    
    elif "Schaedel_nach_C.CT.Knie(Adult).26" in f:
        new_data_folder_path = os.path.join(data_folder_path,r"2. 01_2019\soft_0.2_Br48")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).28" in f:
        new_data_folder_path = os.path.join(data_folder_path,r"2. 01_2019\0.4_Qr40")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
# 08_2017 

    elif "Schaedel_nach_C.CT.Knie(Adult).27" in f:
        new_data_folder_path = os.path.join(data_folder_path,r"3. 08_2017\bone_0.2_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).29" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\bone_0.2_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))     
    # elif "Schaedel_nach_C.CT.Knie(Adult).30" in f:
    #     new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\bone_0.2_Br80")
    #     shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).31" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\bone_0.4_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).32" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\bone_0.4_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).33" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\bone_0.4_Br80")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).34" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\soft_0.2_Br44")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).35" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\soft_0.2_Br48")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).37" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"3. 08_2017\0.4_Qr40")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
# 18_2018
    elif "Schaedel_nach_C.CT.Knie(Adult).36" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.2_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).38" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.2_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))     
    # elif "Schaedel_nach_C.CT.Knie(Adult).39" in f:
    #     new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.2_Br80")
    #     shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).40" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.4_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).41" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.4_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).42" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\bone_0.4_Br80")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).43" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\soft_0.2_Br44")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).44" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\soft_0.2_Br48")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).46" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"4. 18_2018\0.4_Qr40")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
# 08_2017R 
    elif "Schaedel_nach_C.CT.Knie(Adult).45" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.2_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).47" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.2_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))     
    # elif "Schaedel_nach_C.CT.Knie(Adult).48" in f:
    #     new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.2_Br80")
    #     shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).49" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.4_Br72")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).50" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.4_Br68")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))  
    elif "Schaedel_nach_C.CT.Knie(Adult).51" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\bone_0.4_Br80")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).52" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\soft_0.2_Br44")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f)) 
    elif "Schaedel_nach_C.CT.Knie(Adult).53" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\soft_0.2_Br48")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))
    elif "Schaedel_nach_C.CT.Knie(Adult).54" in f:
        new_data_folder_path = os.path.join(data_folder_path, r"5. 08_2017R\0.4_Qr40")
        shutil.copy2(os.path.join(data_folder_path,f), os.path.join(new_data_folder_path,f))   


