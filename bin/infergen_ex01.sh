#!/usr/bin/env bash
# tmp_model이 비어 있는가?
  # 비어 있으면 오류
# 비어 있지 않으면 print_wv에 ex_home 주고 실행

cd ..

# Config 체크
if [ ! -e config_ex01.json ]; then
    echo Error: Configuration Not exist
    exit 9
fi

# Json 파싱
EX_HOME=$(cat config.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}

# TMPDATA 확인
if [ ! -d ${EX_HOME}/ex01/tmp_model ]; then
    echo Error: Temp Model Empty
    exit 8
fi

# 모델 훈련
EX_HOME=${EX_HOME}/ex01
python ex01_infergen.py ${EX_HOME}
