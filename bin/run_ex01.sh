# 첫번째 실험: 맥락 분리의 필요성 (의존성검사 -> 데이터추출 -> 모델 제작 -> 결과 추출)

# 01. 의존성 검사
cd ..
python check_dependency.py

# 02. 데이터 추출 데이터 체크, 다운로드, 전처리, $EX_HOME/(실험번호)/tmp에 저장(각 실험군별로)
python make_data.py