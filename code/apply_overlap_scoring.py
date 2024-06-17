from utils import AnalyzeVolume
import os
import pdb
import SimpleITK as sitk

root_folder_pcct = r'E:\closed_elastix_cartilages3'
root_folder_pcct_images = os.listdir(root_folder_pcct)

for image in root_folder_pcct_images:
    if os.path.splitext(image)[1] == '.nii':
        knee = image.split('_')[0] + '_' + image.split('_')[1]
        gt = os.path.join(r'E:\segmentations MR Tim', knee, image[:-4] + '.nrrd')
        pred = os.path.join(root_folder_pcct, image)
        
        gt_itk = sitk.ReadImage(gt)
        
        pred_itk = sitk.ReadImage(pred)
       

        resample = sitk.ResampleImageFilter()
        resample.SetOutputSpacing(gt_itk.GetSpacing())
        resample.SetSize(gt_itk.GetSize())
        resample.SetOutputDirection(gt_itk.GetDirection())
        resample.SetOutputOrigin(gt_itk.GetOrigin())
        resample.SetTransform(sitk.Transform())
        resample.SetDefaultPixelValue(gt_itk.GetPixelIDValue())
        resample.SetInterpolator(sitk.sitkNearestNeighbor)
        new_pred_itk = resample.Execute(pred_itk)

        gt_array = sitk.GetArrayViewFromImage(gt_itk)
        pred_array = sitk.GetArrayViewFromImage(new_pred_itk)


        # pdb.set_trace()


        overlap_measures_filter = sitk.LabelOverlapMeasuresImageFilter()
        overlap_measures_filter.Execute(gt_itk, new_pred_itk)
        dsc = overlap_measures_filter.GetDiceCoefficient()
        hausdorff_distance_filter = sitk.HausdorffDistanceImageFilter()
        hausdorff_distance_filter.Execute(gt_itk, new_pred_itk)
        hdd = hausdorff_distance_filter.GetHausdorffDistance()

        print('Dice: \t', dsc, '\n Hausdorff Distance: \t', hdd)# '\n Hausdorff disctance: \t', hdd)

        # pdb.set_trace()
        # analysis = AnalyzeVolume(gt_array, pred_array, fixed_img_name='MR', moving_img_name='PCCT')
        # scores = analysis.evaluation_metrics()
        # print(scores)
        # pdb.set_trace()
        # analysis.create_scatter_plot(scores)
    else:
        continue

 

    





