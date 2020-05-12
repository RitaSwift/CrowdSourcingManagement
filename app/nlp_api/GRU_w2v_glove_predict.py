import keras
from keras.models import load_model

import app.nlp_api.Write as Write
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
import os


os.environ['KERAS_BACKEND'] = 'tensorflow'
MAX_SEQUENCE_LENGTH = 130
EMBEDDING_DIM = 100  # 词向量的大小
MAX_NUM_WORDS = 20000  # 用于构建词向量的词汇表数量
category_dict = {0: 'Security', 1: 'Reliability', 2: 'Performance', 3: 'Lifecycle', 4: 'Usability', 5: 'Capability',
                 6: 'Software Interface'}

def GRU_Glove(x_predict):
    tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)#若被设置为整数，则分词器将被限制为待处理数据集中最常见的num_words个单词
    tokenizer.fit_on_texts(x_predict)#学习出文本的字典
    x_predict = tokenizer.texts_to_sequences(x_predict)#句子转换成单词索引序列
    #为了实现的简便，keras只能接受长度相同的序列输入。因此如果目前序列长度参差不齐，这时需要使用pad_sequences()。
    # 该函数是将序列转化为经过填充以后的一个长度相同的新序列新序列。
    #为序列的最大长度。大于此长度的序列将被截短，小于此长度的序列将在后部填0.
    x_predict = pad_sequences(x_predict, maxlen=MAX_SEQUENCE_LENGTH)
    #.hdf5 Python 中有一系列的工具可以操作和使用 HDF5 数据 使用h5py操作hdf5数据 封装在keras中
    keras.backend.clear_session()
    model = load_model("app/nlp_api/weights.023-1.0000.hdf5")
    y_predict = model.predict(x_predict)
    y_pred = Write.one_hot_reverse(y_predict)
    for i in range(len(y_pred)):
        y_pred[i] = category_dict[y_pred[i]]
    # print(y_pred)
    return y_pred


# DATA = [['when', 'the', 'mouse', 'be', 'hold', 'motionles', 'ov', 'the', 'password', 'column', 'have', 'a', 'row', 'reveal', 'the', 'password', 'in', 'a', 'balloon']]
DATA = ['It Would be beautiful to see a web interface to autoap in dd-wrt']
# DATA = ['It','Would','be','beautiful','to','see','a','web','interface','to', 'autoap','in', 'dd-wrt']
GRU_Glove(DATA)

# DATA = ['我是一个小精灵鬼，是真的，是真的，真的']
# GRU_Glove(DATA)