import json
import os

from konlpy.tag import Okt

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry
from tensor2tensor.models.transformer import transformer_base_v1
from tensor2tensor.models.transformer import transformer_base_v1


class Reader(object):
    def __init__(self, file_list, shuffle=True, total=None):
        self.file_list = file_list
        self.total = total  # if not total -> 무제

    def parse(self, file):
        # JSON 읽어서 라인 딕트로 리턴 -> 제너레이터
        pass

    def generate(self):
        for file in file_list:
            pass
        pass    # JSON 파싱해서 yield

@registry.register_hparams('hparam_transformer_t2t')
def hparam_transformer_t2t():
    hp = transformer_base_v1()
    #hp.hidden_size = 256
    hp.summarize_vars = True
    return hp

@registry.register_problem('transformer_t2t')
class transformer_t2t(text_problems.Text2TextProblem):
    @property
    def dataset_splits(self):
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 100,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 20,
        }]

    @property
    def is_generate_per_split(self):
        return True

    @property
    def approx_vocab_size(self):
        return 2**15

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        data_file_list = [file for file in os.listdir(data_dir) if file.endswith('.json')]
        div = 'train'
        # total = 200
        reader = Reader(
            file_list=data_file_list,
            shuffle=True,
            total=total
        )
        for data in reader.generate():
            yield data