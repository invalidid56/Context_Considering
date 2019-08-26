#!/usr/bin/env bash
# EX_HOME tmp_data 비어 있는가?
  # 비어 있으면 오류
# 워드벡터 빌드, build_wv에 EX_HOME을 준다 tmp_model에 출력

cd ..

# Config 체크
if [ ! -e config_ex01.json ]; then
    echo Error: Configuration Not exist
    exit 9
fi

# Json 파싱
EX_HOME=$(cat config_ex01.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}

# TMPDATA 확인
if [ ! -d ${EX_HOME}/ex01/tmp_data ]; then
    echo Error: Temp Data Empty
    exit 8
fi

# 모델 훈련
python train.py
