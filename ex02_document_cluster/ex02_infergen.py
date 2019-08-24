import json
import os
import pickle
from glob import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import decomposition
from sklearn.preprocessing import normalize

def main():
    with open('config_ex02.json') as conf:
        config = json.load(conf)
        EX_HOME = os.path.join(config['EX_HOME'], 'ex02')


    def file2list(filename):
        with open(filename, 'rb') as f:
            rawdata = []
            while True:
                try:
                    l = pickle.load(f)
                    l = ' '.join(l)
                    rawdata.append(l)
                except EOFError:
                    break
        return '\n'.join(rawdata)


    def init_data():
        target = os.path.join(EX_HOME, 'tmp_data', 'process_*.bin')
        files = glob(target)
        return map(file2list, files)


    def decompose_by_nmf(debug=True):
        initdata = init_data()

        vectorizer = CountVectorizer()
        counts = vectorizer.fit_transform(initdata)
        tfidf = TfidfTransformer().fit_transform(counts)

        nmf = decomposition.NMF(n_components=7).fit(tfidf)
        feature_names = vectorizer.get_feature_names()

        print("features 7")
        if debug:
            for topic_idx, topic in enumerate(nmf.components_):
                print("Topic #%d:" % topic_idx)
                print(" ".join([feature_names[i] for i in topic.argsort()[:-100:-1]]))  # TODO: Print As File

    decompose_by_nmf()


if __name__ == '__main__':
    main()