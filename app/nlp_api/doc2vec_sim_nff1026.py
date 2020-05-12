import numpy as np
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

# train the corpus to obtain doc2vec model
from app.nlp_api.read import Read


def train_d2v_model(filename):
    corpus = Read(filename)
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(corpus)]
    model = Doc2Vec(documents, vector_size=100, window=8, min_count=0, workers=4)  # 基于所有需求训练doc2vec模型
    model.save("doc2vec_model")
    return model


# load the pre-trained model to transform one piece of request into vector
def d2v_vector(request):
    model = Doc2Vec.load('doc2vec_model')
    vector = model.infer_vector(request)
    return vector


# cosine similarity
def cosine_sim(vecA, vecB):
    """Find the cosine similarity distance between two vectors."""
    csim = np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB))
    if np.isnan(np.sum(csim)):
        return 0
    return csim


# euclidean similarity
def euclidean_sim(p, q):
    e = sum([(p[i] - q[i])**2 for i in range(len(p))])
    return 1/(1+e**.5)


# 只计算两者共同有的
# 计算曼哈顿距离
def manhattan_sim(p, q):
    n = p
    vals = range(len(n))
    distance = sum(abs(p[i] - q[i]) for i in vals)
    return 1/(1+distance)

#中文
# train_d2v_model("keepass.txt")
# vector1 = d2v_vector(list("具有登录和注册的功能"))
# vector2 = d2v_vector(list("具有登录和注册的功能"))
# print("cosine similarity:")
# print(cosine_sim(vector1, vector2))
# print("euclidean similarity: ")
# print(euclidean_sim(vector1, vector2))
# print("manhattan_sim similarity: ")
# print(manhattan_sim(vector1, vector2))

# train_d2v_model("keepass.txt")
# vector1 = d2v_vector(list("具有登录和注册的功能"))
# vector2 = d2v_vector(list("具有登录和注册的功能啦"))
# print("cosine similarity:")
# print(cosine_sim(vector1, vector2))
# print("euclidean similarity: ")
# print(euclidean_sim(vector1, vector2))
# print("manhattan_sim similarity: ")
# print(manhattan_sim(vector1, vector2))

# train_d2v_model("keepass.txt")
# vector1 = d2v_vector(list("With login and registration functions"))
# vector2 = d2v_vector(list("With login and registration functions"))
# print("cosine similarity:")
# print(cosine_sim(vector1, vector2))
# print("euclidean similarity: ")
# print(euclidean_sim(vector1, vector2))
# print("manhattan_sim similarity: ")
# print(manhattan_sim(vector1, vector2))

# train_d2v_model("keepass.txt")
# vector1 = d2v_vector(list("With login and registration functions"))
# vector2 = d2v_vector(list("have login and registration functions"))
# print("cosine similarity:")
# print(cosine_sim(vector1, vector2))
# print("euclidean similarity: ")
# print(euclidean_sim(vector1, vector2))
# print("manhattan_sim similarity: ")
# print(manhattan_sim(vector1, vector2))