# wv 읽어와서 시각
# 대명사 의미|  맥락분리시 단어일관성, 맥락통합 단어일관성 비교

from gensim.models import Word2Vec
from sklearn.manifold import TSNE

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

import json
import sys
import os
from matplotlib import font_manager, rc


def main():
    with open('config.json') as jsf:
        config = json.load(jsf)
        targets = config['TARGET']
    EX_HOME = sys.argv[1]

    models = ['model_'+str(i) for i in range(5)]
    sample = [Word2Vec.load(os.path.join(EX_HOME, 'tmp', file)) for file in models]


    def draw_plt(model):  # TODO: Cannot Print Korean
        vocab = list(model.wv.vocab)
        X = model[vocab]
        tsne = TSNE(n_components=2)
        X_tsne = tsne.fit_transform(X[:500, :])
        df = pd.DataFrame(X_tsne, index=vocab[:500], columns=['x', 'y'])

        fig = plt.figure()
        fig.set_size_inches(40, 20)
        ax = fig.add_subplot(1, 1, 1)

        ax.scatter(df['x'], df['y'])

        for word, pos in df.iterrows():
            ax.annotate(word, pos, fontsize=30)

        return fig

    for i, model in enumerate(sample):
        with open(os.path.join(EX_HOME, 'result_'+str(i)+'.txt'), 'w') as f:
            for word in targets:
                sim = model.wv.most_similar(word)
                result = word+'\n'+'----------------------\n'+'\n'.join([str(s) for s in sim])
                f.write(result)
        fig = draw_plt(model)
        fig.savefig(os.path.join(EX_HOME, 'result_'+str(i)+'.png'))

if __name__ == '__main__':
    main()
