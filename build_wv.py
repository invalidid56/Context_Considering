# 파일 읽어와서 wv 구축

import pprint
from gensim.test.utils import get_tmpfile
from gensim.models.word2vec import Word2Vec
import pickle
import json
import os
import sys


def main():
    # 인자에서 코퍼스 읽어오기기 -> 읽어오고 지우
    # 코퍼스별로 피클 읽어서 워드벡터 만들고
    # 워드벡터 tmp에다 저장하기기

    EXP_HOME = sys.argv[1]
    corpus_list = [file for file in sorted(os.listdir(os.path.join(EXP_HOME, 'tmp')))
                    if file.endswith('.bin')]
    def make_wv(filedir):
        corpus = []
        with open(filedir, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    print(line)
                    corpus.append(line)
                except EOFError:
                    break
        model = Word2Vec(corpus, min_count=1)
        return model
    for i, corpus in enumerate(corpus_list):
        wv = make_wv(os.path.join(EXP_HOME, 'tmp', corpus))
        wv.save(os.path.join(EXP_HOME, 'tmp', 'model_'+str(i)))

if __name__ == '__main__':
    main()