#!/usr/bin/env bash

cd ..

# Config 체크
if [ ! -e config_ex01.json ]; then
    echo Error: Configuration Not exist
    exit 9
fi

# Json 파싱
EX_HOME=$(cat config_ex01.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}

# TMPMODEL 확인
if [ ! -d ${EX_HOME}/ex01/tmp_model ]; then
    echo Error: Temp Model Empty
    exit 8
fi

# 결과 출력
python infergen.py
