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

FILECNT=$(ls $TMP_DIR | wc -l)

if [ $FILECNT = 0 ] ; then
    echo '>>>> Start Datagen for Training.'

    python train.py \
      --data_dir=$DATA_DIR \
      --output_dir=$TMP_DIR \
      --problem=$PROBLEM \
      --hparams_set=$HPARAMS \
      --model=$MODEL

    echo '>>>> End Datagen for Training.'
else
    echo '>>>> Dataset files are already exist in target dir. Check and try datagen again.'
fi
