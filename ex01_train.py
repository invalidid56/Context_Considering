import os
import sys
import pickle
import json
import logging
from gensim.models.word2vec import Word2Vec


def main():
    # 임시데이터 목록 불러오기
    with open('config_ex01.json') as conf:
        config = json.load(conf)
        EX_HOME = os.path.join(config['EX_HOME'], 'ex01')
    corpus_list = [file for file in sorted(os.listdir(os.path.join(EX_HOME, 'tmp_data')))
                    if file.endswith('.bin')]

    # 로그 설정
    logger = logging.getLogger(__name__)
    log_file = os.path.join(EX_HOME, 'ex_log.log')
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
    filehandler = logging.FileHandler(log_file)
    logger.addHandler(filehandler)
    logger.setLevel(level=logging.DEBUG)

    # 모델 훈련 함수 정의
    def make_wv(filedir):
        corpus = []
        with open(filedir, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    corpus.append(line)
                except EOFError:
                    break
        model = Word2Vec(corpus, min_count=1)
        return model

    # 모델 훈련 후 저장
    for i, corpus in enumerate(corpus_list):
        wv = make_wv(os.path.join(EX_HOME, 'tmp_data', corpus))
        wv.save(os.path.join(EX_HOME, 'tmp_model', 'model_'+str(i)))
        logger.info('WV Model Saved: '+os.path.join(EX_HOME, 'tmp_model', 'model_'+str(i)))

if __name__ == '__main__':
    main()