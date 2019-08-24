from konlpy.tag import Okt

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry
from tensor2tensor.models.transformer import transformer_base_v1
from t2t.problems_with_infer import Text2TextProblemWithInfer, Text2ClassProblemWithInfer
from tensor2tensor.models.transformer import transformer_base_v1


class Reader(object):
    def generate(self):
        pass    # JSON 파싱해서 yield

@registry.register_hparams('hparam_transformer_t2t')
def hparam_transformer_t2t:
    hp = transformer_base_v1()
    #hp.hidden_size = 256
    hp.summarize_vars = True
    return hp

@registry.register_problem('transformer_t2t')
class transformer_t2t(Text2TextProblemWithInfer):
    """Kakaoarena shopping goods info classification - only with products, by words"""

    @property
    def vocab_type(self):
        return text_problems.VocabType.SUBWORD

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 100,
        }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 10,
      }]

    @property
    def approx_vocab_size(self):
        return 2 ** 16  # ~64k

    @property
    def approx_target_vocab_size(self):
        return 2 ** 12  # ~4k

    @property
    def is_generate_per_split(self):
      # generate_data will shard the data into TRAIN and EVAL for us.
        return True

    def get_reader(self, data_dir, tmp_dir, dataset_split):
        if dataset_split == problem.DatasetSplit.TRAIN:
            div = 'train'
        else:
            div = 'dev'
            data_path_list = get_data_file_list(data_dir, div)
            total = get_total_data_count(data_path_list, 'train')
            return Reader(data_path_list, 'train', 0, total, word=True)