# 데이터 체크, 다운로드, 전처리, $EX_HOME/(실험번호)/tmpdir에 저장

from konlpy.tag import Okt
import sys
import os
import pickle

def main():
    tag = Okt()
    DATA_HOME, EX_HOME, SHEET_HOME = sys.argv[1:3]


    # 데이터 체크, else 다운로드 

    # 시트에서 각 실험군 코퍼스 정보 불러오기
    if not os.path.exists(os.path.join(SHEET_HOME, 'sheet')):
        print('ERROR: CANNOT READ SHEET')
        sys.exit(9)
    else:
        with open(os.path.join(SHEET_HOME, 'sheet')) as f:
            copora = []
            while True:
                if not f.readline():
                    break
                copora.append(f.readline())

    # 각 실험군별로 전처리된 하나의 코퍼스 만들기
    def make_gen(filedir):
        with open(os.path.join(DATA_HOME, filedir), 'rb'):
            while True:
                line = f.readline()
                try:
                    line = line.decode('euc-kr')
                except UnicodeDecodeError:
                    try:
                        line = line.decode('utf-8')
                    except:
                        continue
                if not line:
                    f.close()
                    break
                line = line.replace('\r\n', '').replace('\n', '')
                if not (line.startswith('<') or line == ''):
                    line = mor.morphs(line)
                    if not line == []:
                        yield line
                    else:
                        continue

    # EXHOME 아래 TMPDIR에 저장
    os.makedirs(os.path.join(EX_HOME, 'tmp'))
    for i, corpus in enumerate(copora):
        with open(os.path.join(EX_HOME, 'tmp', 'process_'+str(i)+'.bin'), 'wb') as f:
            gen = make_gen(os.path.join(DATA_HOME, corpus))
            for line in gen:
                pickle.dump(line, f)
