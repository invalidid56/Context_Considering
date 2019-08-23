# wv 읽어와서 시각
'''
정해진 실험군/대조군에서 코퍼스 혼합 비율에 따라 make_corpus.py 같은거 만들든지 해서 시트에 6개 군 입력
중점적으로 보여줄 것: 대명사에서 유추되는 단어/ 단어가 갖는 의미가 일관되는지
어떻게? 워드벡터 시각화 / 타겟단어 가장 근접한 단어 출력
'''
# 대명사 의미|  맥락분리시 단어일관성, 맥락통합 단어일관성 비교

import json
import os
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc


def main():

    font_name = font_manager.FontProperties(fname='/usr/share/fonts/NanumFont/NanumGothic.ttf').get_name() # TODO: Font Dependency
    rc('font', family=font_name)
    mpl.rcParams['axes.unicode_minus'] = False

    with open('config_ex01.json') as jsf:
        config = json.load(jsf)
        targets = config['TARGET']
        EX_HOME = os.path.join(config['EX_HOME'], 'ex01')

    # 로그 설정
    logger = logging.getLogger(__name__)
    log_file = os.path.join(EX_HOME, 'ex_log.log')
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
    filehandler = logging.FileHandler(log_file)
    logger.addHandler(filehandler)
    logger.setLevel(level=logging.DEBUG)

    models = ['model_'+str(i) for i in range(5)]
    sample = [Word2Vec.load(os.path.join(EX_HOME, 'tmp_model', file)) for file in models]


    def draw_plt(model):  # TODO: Cannot Print Korean
        vocab = list(model.wv.vocab)
        X = model[vocab]
        tsne = TSNE(n_components=2)
        X_tsne = tsne.fit_transform(X[:500, :])  # 500까지만
        df = pd.DataFrame(X_tsne, index=vocab[:500], columns=['x', 'y'])
        fig = plt.figure()
        fig.set_size_inches(40, 20)
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(df['x'], df['y'])
        for word, pos in df.iterrows():
            ax.annotate(word, pos, fontsize=30)
        return fig

    def infer_data(model, targets):
        result = []
        for word in targets:
            sim = model.wv.most_similar(word)
            result.append(word + '\n' + '----------------------\n' + '\n'.join([str(s) for s in sim]))
        return result


    for i, model in enumerate(sample):
        output = 'result_'+str(i)
        infer_data(model, targets)
        with open(os.path.join(EX_HOME, output+'.txt'), 'w') as f:
            f.write('\n\n'.join(infer_data(model, targets)))
        fig = draw_plt(model)
        fig.savefig(os.path.join(EX_HOME, output+'.png'))

if __name__ == '__main__':
    main()
