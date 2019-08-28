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

mkdir -p  $TMP_DIR

python train.py \
    --data_dir=$DATA_DIR \
    --output_dir=$TMP_DIR \
    --problem=$PROBLEM \
    --hparams_set=$HPARAMS \
    --hparams='batch_size=1024' \
    --model=$MODEL \
    --eval_steps=100 \
    --worker_gpu=4


