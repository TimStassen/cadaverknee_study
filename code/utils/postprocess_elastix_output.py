# from SimpleITK import BinaryMorphologicalClosingImageFilter
import os
import SimpleITK as sitk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pdb

# set MPLBACKEND=qtagg


def postprocess_elastix_output(input_file, result_path):

    
    myFilter = sitk.BinaryMorphologicalClosingImageFilter()
    myFilter.SetDebug(False)
    myFilter.SetForegroundValue(1.0)
    myFilter.SetKernelRadius((5, 5, 5))
    myFilter.SetKernelType(1)
    myFilter.SetNumberOfThreads(16)
    myFilter.SetNumberOfWorkUnits(0)
    myFilter.SetSafeBorder(True)


    itk_image = sitk.ReadImage(input_file)
    closed_img = myFilter.Execute(itk_image)
    filename = input_file.split('\\')[2]
    anatomical_struct = filename.split('_')[2]
    if anatomical_struct == 'femur':
            filename = filename.split('_')[0] + '_' + filename.split('_')[1] +'_femoral_cartilage'
    elif anatomical_struct == 'tibia':
        filename = filename.split('_')[0] + '_' + filename.split('_')[1] +'_tibial_cartilage'
    elif anatomical_struct == 'patella':
        filename = filename.split('_')[0] + '_' + filename.split('_')[1] +'_retro_patellar_cartilage'
    else: 
        cartilage = ''
    # pdb.set_trace()
    sitk.WriteImage(closed_img, os.path.join(result_path,filename + '.mhd'))

if __name__ == "__main__":
    root_folder = r'E:\registration_results_FINAL4'
    dir_list = os.listdir(root_folder)
    results_path = r'E:\closed_elastix_cartilages4'
    if os.path.exists(results_path) is False:
                    os.mkdir(str(results_path))

    for scan in dir_list:
        transformed_file = os.path.join(root_folder, scan, 'transformix_results0', 'result.mhd')
        postprocess_elastix_output(transformed_file, results_path)



