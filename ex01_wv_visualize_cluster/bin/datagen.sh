#!/usr/bin/env bash

cd ..

# Config 체크
if [ ! -e "config_ex01.json" ]; then
    echo Error: Configuration Not exist
    exit 9
else
    # Json 파싱
    EX_HOME=$(cat config_ex01.json | jq .EX_HOME)
    EX_HOME=${EX_HOME:1:-1}

    # 이전 결과 삭제
    if [ -d ${EX_HOME}/ex01 ]; then
        rm  -r ${EX_HOME}/ex01/
    fi

    # 실험 디렉터리 생성
    EX_HOME=${EX_HOME}/ex01
    mkdir -p ${EX_HOME}

    # 임시데이터 생성
    python datagen.py
fi
