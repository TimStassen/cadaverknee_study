from utils import AnalyzeVolume
import os
import pdb
import SimpleITK as sitk

root_folder_pcct = r'D:\closed_elastix_cartilages'
root_folder_pcct_images = os.listdir(root_folder_pcct)

# for image in root_folder_pcct_images:
image = '30_2017_tibial_cartilage.nii'
# pdb.set_trace()
if os.path.splitext(image)[1] == '.nii':
    knee = image.split('_')[0] + '_' + image.split('_')[1]
    gt = os.path.join(r'D:\segmentations MR Tim', knee, image[:-4] + '.nrrd')
    pred = os.path.join(root_folder_pcct, image)
    
    gt_itk = sitk.ReadImage(gt)
    pred_itk = sitk.ReadImage(pred)
    

    # resample = sitk.ResampleImageFilter()
    # resample.SetOutputSpacing(gt_itk.GetSpacing())
    # resample.SetSize(gt_itk.GetSize())
    # resample.SetOutputDirection(gt_itk.GetDirection())
    # resample.SetOutputOrigin(gt_itk.GetOrigin())
    # resample.SetTransform(sitk.Transform())
    # resample.SetDefaultPixelValue(gt_itk.GetPixelIDValue())
    # resample.SetInterpolator(sitk.sitkNearestNeighbor)
    new_pred_itk = sitk.Resample(pred_itk, gt_itk)

    # pdb.set_trace()
    if new_pred_itk.GetSpacing() != gt_itk.GetSpacing():
        ValueError('Dimension mismatch in predicted image and ground truth image ')

    # gt_array = sitk.GetArrayViewFromImage(gt_itk)
    # pred_array = sitk.GetArrayViewFromImage(new_pred_itk)


    # remove distoring values (0 and 1 only)
    pred_thresh = new_pred_itk > 0
    gt_thresh = gt_itk > 0

    # # pdb.set_trace()
    print('MR file: \t', gt)
    print('PCCT file: \t', pred)

    overlap_measures_filter = sitk.LabelOverlapMeasuresImageFilter()
    hausdorff_distance_filter = sitk.HausdorffDistanceImageFilter()

    overlap_measures_filter.Execute(gt_thresh, pred_thresh)
    jaccard = overlap_measures_filter.GetJaccardCoefficient()
    DSc = overlap_measures_filter.GetDiceCoefficient()
    volume = overlap_measures_filter.GetVolumeSimilarity()
    Fn = overlap_measures_filter.GetFalseNegativeError()
    Fp = overlap_measures_filter.GetFalsePositiveError()
    # Hausdorff distance
    # pdb.set_trace()
    hausdorff_distance_filter.Execute(gt_thresh, pred_thresh)
    Hdd = hausdorff_distance_filter.GetHausdorffDistance()

    
    print('Jaccard:', jaccard)
    print('DSC:', DSc)
    print('Volume:', volume)
    print('False Negatives:', Fn)
    print('False Positives:', Fp)
    print('Hausdorff Distance:', Hdd)
    
# else:
    # continue









