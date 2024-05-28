from __future__ import print_function, absolute_import

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial.distance import directed_hausdorff
from sklearn.metrics import confusion_matrix
from collections import Counter
import pdb


class AnalyzeVolume:
    def __init__(self, GT_list, pred_list, fixed_img_name, moving_img_name):
        self.GT_list = GT_list
        self.pred_list = pred_list
        self.fixed_img_name = fixed_img_name
        self.moving_img_name = moving_img_name

    def evaluation_metrics(self):
        "Make sure the list indices of inputs (pred_list and true_list) are nd.arrays"

        result_list = []
        # fixed_image = []
        # moving_image = []
        for pred, GT, fixed_name, moving_name in zip(self.pred_list, self.GT_list, self.fixed_img_name, self.moving_img_name):
            pred_flat = np.ndarray.flatten(pred)
            true_flat = np.ndarray.flatten(GT)

            mcm = confusion_matrix(pred_flat, true_flat)
            tn = mcm[0, 0]
            fp = mcm[0, 1]
            fn = mcm[1, 0]
            tp = mcm[1, 1]

            # Compute the evaluation metrics.
            Sensitivity = tp / (tp + fn)
            Specificity = tn / (tn + fp)
            Accuracy = (tp + tn) / (tp + tn + fn + fp)
            Dice_score = 2 * tp / (2 * tp + fp + fn)
            pdb.set_trace()
            Precision = tp / (tp + fp)
            Recall = tp / (tp + fn)
            F1 = 2 * (Recall * Precision) / (Recall + Precision)


            dict = {'fixed_image': fixed_name, 
                    'moving_image': moving_name,
                    'Sensitivity': Sensitivity,
                    'Specificity': Specificity,
                    'Accuracy': Accuracy,
                    'Dice_score': Dice_score,
                    'F1': [F1]}

            result_list.append(dict)
        return result_list


    # def create_df(self, inner_loop_pred_segm, inner_loop_gt_segm, train_set):
    #     # Create dataframe to save evaluation metrics
    #     cols = ['Sensitivity','Specificity','Accuracy','Dice_score','F1', 'p-number']
    #     df_evaluation = pd.DataFrame(columns=cols)

    #     df_evaluation = evaluation_metrics(df_evaluation, inner_loop_pred_segm, inner_loop_gt_segm, train_set)
    #     print(df_evaluation)
    #     return df_evaluation


    def create_scatter_plot(self, dict, plot_name, moving_image):
        
        sensitivity = dict['Sensitivity'].tolist()
        specificity = dict['Specificity'].tolist()
        accuracy = dict['Accuracy'].tolist()
        dice_score = dict['Dice_score'].tolist()
        images = dict['p-number'].tolist()

        plt.scatter(images,sensitivity, label = 'Sensitivity')
        plt.scatter(images,specificity, label = 'Specificity')
        plt.scatter(images, accuracy, label = 'Accuracy')
        plt.scatter(images, dice_score, label = 'Dice score')
        plt.legend(loc='lower right')
        plt.xlabel('Image Number')
        plt.title(plot_name+moving_image[0])
        plt.savefig(plot_name+moving_image[0])
        
        return None


    def create_box_plot(self, df, plot_name, moving_image):
        metrics = list(df.columns)
        
        sensitivity = df['Sensitivity'].tolist()
        specificity = df['Specificity'].tolist()
        accuracy = df['Accuracy'].tolist()
        dice_score = df['Dice_score'].tolist()
        data = [sensitivity, specificity, accuracy, dice_score]
        plt.boxplot(data)

        
        plt.xticks([1, 2, 3, 4], metrics[:4])
        plt.title(plot_name+moving_image[0])
        plt.savefig(plot_name+moving_image[0])
        plt.show()
        
        for i in range(len(data)):
            print('For', metrics[i], ',the average is:', np.mean(data[i]), 'and the std is:', np.std(data[i]))
        return None

if __name__ == "__main__":

    GT_vol1 = np.array([[1, 0, 0], [0, 1, 1], [0, 1, 1]])
    GT_vol2 = np.array([[1, 1, 0], [0, 0, 1], [0, 1, 0]])
    GT_vol3 = np.array([[0, 0, 0], [1, 1, 1], [0, 1, 1]])
    GT_tot = [GT_vol1, GT_vol2, GT_vol3]

    pred_vol1 = np.array([[1, 1, 0], [0, 1, 1], [0, 0, 1]]) # acc = 7/9
    pred_vol2 = np.array([[1, 1, 0], [0, 0, 1], [1, 1, 0]]) #
    pred_vol3 = np.array([[1, 0, 0], [1, 0, 1], [0, 1, 0]]) #
    pred_tot = [pred_vol1, pred_vol2, pred_vol3]

    fixed_names = ['fixed_array1', 'fixed_array2', 'fixed_array3']
    moving_names = ['moving_array1', 'moving_array2', 'moving_array3']

    a = AnalyzeVolume(GT_tot, pred_tot, fixed_names, moving_names)
    all_metrics = a.evaluation_metrics()
    metrics = all_metrics[0]
    pdb.set_trace()
    # print('fixed image:', metrics['fixed_image'], '\n moving image:', metrics['moving_image'], '\n DSC:',  metrics['Dice_score'])
    print("fixed image:", metrics['fixed_image'], "\n moving image:", metrics['moving_image'],  "%.2f" % (metrics['Dice_score']))

