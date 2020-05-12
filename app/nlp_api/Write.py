from operator import truediv
import numpy as np


def P_R_F(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    confusion_matrix = confusion_matrix(y_true, y_pred)
    # print("confusion_matrix: ", confusion_matrix)

    # 计算第i类的precision, recall and F
    diag = np.diag(confusion_matrix)  # 取对角线上的值
    raw_sum = np.sum(confusion_matrix, axis=1)  # 计算每一行的和
    each_acc = np.nan_to_num(truediv(diag, raw_sum))
    # print("recall: ", each_acc)

    column_sum = np.sum(confusion_matrix, axis=0)  # 计算每一列的和
    each_precision = np.nan_to_num(truediv(diag, column_sum))
    # print("precision: ", each_precision)

    F = []
    i = 0
    while i < len(each_precision):
        F.append(2 * each_precision[i] * each_acc[i] / (each_precision[i] + each_acc[i]))
        i = i + 1

    # print("F: ", F)

    return each_acc, each_precision, F


def one_hot_reverse(oneHot):
    result = []
    for k in oneHot:
        r = np.argmax(k)
        result.append(r)
    return result





