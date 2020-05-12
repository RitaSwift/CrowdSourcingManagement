from sklearn.externals import joblib
import json
import numpy as np


def load_model():
    lr_model = joblib.load('app/nlp_api/lr.model')
    with open('app/nlp_api/vocabulary.json', 'r') as f:
        feature_dic = json.load(f)
    with open('app/nlp_api/idf.json', 'r') as f:
        idf_dic = json.load(f)
    return lr_model, feature_dic, idf_dic


def confirm_priority(line):
    line_list = list(map(lambda x: x.split(' '), line))
    predic_feature = [0]*4198
    batch_list = []
    lr_model, feature_dic, idf_dic = load_model()
    for i in range(0, len(line_list)):
        word_list = line_list[i]
        for word in word_list:
            try:
                idf = idf_dic[feature_dic[word]]
                tf = word_list.count(word)
                predic_feature[feature_dic[word]] = tf*idf
                # print(tf*idf)
            except Exception as e:
                pass
        batch_list.append(predic_feature)
    preds = lr_model.predict(np.array(batch_list))
    return preds

