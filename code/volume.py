import trimesh as tm
import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pdb


mask_path = r"D:\segmentations MR Tim\30_2017\30_2017_femoral_cartilage.nrrd"

mask_image = sitk.ReadImage(mask_path)
shape_stats = sitk.LabelShapeStatisticsImageFilter()
shape_stats.Execute(mask_image)
vol_roi = shape_stats.GetPhysicalSize(1)
print(vol_roi)
