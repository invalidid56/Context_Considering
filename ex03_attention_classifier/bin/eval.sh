#!/usr/bin/env bash

#!/usr/bin/env bash

PROBLEM=transformer_t2t
MODEL=transformer
HPARAMS=hparam_transformer_t2t

cd ..
BASEDIR=$(pwd)

EX_HOME=$(cat config_ex03.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}

DATA_DIR=${EX_HOME}/ex03/tmp_data
TMP_DIR=${EX_HOME}/ex03/tmp_model


python eval.py \
    --problem=$PROBLEM \
    --hparams_set=$HPARAMS \
    --model=$MODEL \
    --data_dir=$DATA_DIR \
    --output_dir=$TMP_DIR \
    --eval_use_test_set=False \
    echo '>>>> End Datagen for Training.'

