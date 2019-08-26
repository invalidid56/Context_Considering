import json
import os
import pickle
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import decomposition
from sklearn.preprocessing import normalize
import logging.handlers
import logging

def main():
    with open('config_ex02.json') as conf:
        config = json.load(conf)
        EX_HOME = os.path.join(config['EX_HOME'], 'ex02')

    target = os.path.join(EX_HOME, 'tmp_data', 'process_*.bin')
    files = glob(target)

    def read_binary(filedir):
        corpus = []
        with open(filedir, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    line = ' '.join(line)
                    corpus.append(line)
                except EOFError:
                    break
        return corpus


    def decompose_by_nmf(i, file):
        corpus = read_binary(file)

        vectorizer = CountVectorizer()
        counts = vectorizer.fit_transform(corpus)
        tfidf = TfidfTransformer().fit_transform(counts)

        nmf = decomposition.NMF(n_components=5).fit(tfidf)
        feature_names = vectorizer.get_feature_names()

        with open(os.path.join(EX_HOME, 'result_0'+str(i)+'.txt'), 'w') as f:
            for topic_idx, topic in enumerate(nmf.components_):
                f.write("Topic " + str(topic_idx))
                f.write('==============================================')
                f.write(" ".join([feature_names[i] for i in topic.argsort()[:-100:-1]]))

    for i, f in enumerate(files):
        decompose_by_nmf(i, f)

if __name__ == '__main__':
    main()