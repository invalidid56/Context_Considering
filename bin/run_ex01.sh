# 첫번째 실험: 맥락 분리의 필요성 (의존성검사 -> 데이터추출 -> 모델 제작 -> 결과 추출)

# 01. 의존성 검사
cd ..
python check_dependency.py

EX_HOME=$(cat config.json | jq .EX_HOME)
EX_HOME=${EX_HOME:1:-1}
TIME=`date +%Y%m%d%H%M%S`
mkdir -p "$EX_HOME"/exp_"$TIME"/tmp  # 결과 저장 경로 생성

# 02. 데이터 추출 데이터 체크, 다운로드, 전처리, $EX_HOME/(실험번호)/tmp에 저장(각 실험군별로) 그리고 corpus로 옮기
if [ ! -d $EX_HOME/corpus ] ; then
    python ex01_datagen.py $EX_HOME/exp_"$TIME"
    mkdir -p $EX_HOME/corpus
    cp $EX_HOME/exp_"$TIME"/tmp/process* $EX_HOME/corpus
else
  cp $EX_HOME/corpus/* $EX_HOME/exp_"$TIME"/tmp
fi

#03. 워벡 체크, 워드벡터 제작, 모델 제작 그리고 wv로 옮기
if [ ! -d $EX_HOME/wv ] ; then
  python ex01_train.py $EX_HOME/exp_"$TIME"
  mkdir -p $EX_HOME/wv
  cp $EX_HOME/exp_"$TIME"/tmp/model* $EX_HOME/wv
else
  cp $EX_HOME/wv/* $EX_HOME/exp_"$TIME"/tmp
fi

#04. 모델 불러와서 결과 작성, 시각화 출력(EX_HOME 아래에 군번_result.txt, 군번_result.png 형태로)기
python ex01_infergen.py $EX_HOME/exp_"$TIME"