# 첫번째 실험: 맥락 분리의 필요성 (의존성검사 -> 데이터추출 -> 모델 제작 -> 결과 추출)

# 01. 의존성 검사
cd ..
python check_dependency.py

EX_HOME=$(cat config.json | jq .EX_HOME)
TIME=`date +%Y%m%d%H%M`
mkdir -p "$EX_HOME"/exp_"$TIME"  # 결과 저장 경로 생성
EX_HOME=$EX_HOME/exp_$TIME
DATA_HOME=$(cat config.json | jq .DATA_HOME)

# 02. 데이터 추출
python make_data.py  # 데이터 체크, 다운로드, 전처리, $EX_HOME/(실험번호)/tmpdir에 저장(각 실험군별로)
# 인자: DATA_HOME, EX_HOME, SHEET_HOME
