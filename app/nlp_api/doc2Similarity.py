import numpy as np
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

# train the corpus to obtain doc2vec model
from app.nlp_api.read import Read


def _d2v_model(corpus):
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(corpus)]
    # 基于所有需求训练doc2vec模型
    model = Doc2Vec(documents, vector_size=100, window=8, min_count=0, workers=4)
    model.save("doc2vec_model")
    return model


# load the pretrained model to transform one piece of request into vector
def _d2v_vector(request, model_dir):
    model = Doc2Vec.load(model_dir)
    vector = model.infer_vector(request)
    return vector


# load the pretrained model to transform all piece of requests into vectors
def _ds2v_vector(requests, model_dir):
    model = Doc2Vec.load(model_dir)
    vectors = list(map(lambda x: model.infer_vector(x), requests))
    return vectors


# cosine similarity
def _cosine_sim(vecA, vecs):
    """Find the cosine similarity distance between two vectors."""
    # vecA = np.broadcast_to(vecA, vecB.shape)
    vecA = vecA.reshape(1, 100)
    csim = np.dot(vecs, vecA.T) / (np.linalg.norm(vecA, axis=1, keepdims=True) *
                                   np.linalg.norm(vecs, axis=1, keepdims=True))
    csim = np.nan_to_num(np.sum(csim, axis=1))
    return csim


# euclidean similarity
def _euclidean_sim(p, vecs):
    e = 1 / (1 + np.sqrt(np.sum(np.square(p - vecs), axis=1)))
    return e


def _manhattan_sim(p, vecs):
    # 只计算两者共同有的
    # 计算曼哈顿距离
    distance = 1 / (1 + np.sum(np.abs(p - vecs), axis=1))
    return distance


def load_data_and_save(data_dir="keepass.txt", save_dir="vecs.np"):
    requires = Read(data_dir)
    _d2v_model(requires)
    vecs = _ds2v_vector(requires, "doc2vec_model")
    np.save(save_dir, vecs)
    return vecs


# if __name__ == "__main__":
#     start = time.time()
#     # vs = load_data_and_save()
#     vs = np.load("vecs.np.npy")  # 所有需要计算相似度的vector
#     cos = []
#     man = []
#     euc = []
#     for v in vs:
#         cos.append(_cosine_sim(v, vs))  # 计算当前vector与所有vector的cosine similarity
#         man.append(_manhattan_sim(v, vs))  # 计算当前vector与所有vector的manhattan similarity
#         euc.append(_euclidean_sim(v, vs))  # 计算当前vector与所有vector的euclidean similarity
#     stop = time.time()
#     # print(cos)
#     # print(man)
#     # print(euc)
#     print(stop - start)
