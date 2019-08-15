# 데이터 체크, 다운로드, 전처리, $EX_HOME/(실험번호)/tmpdir에 저장

from konlpy.tag import Okt
import sys
import os
import pickle
import json

def main():
    tag = Okt()
    with open('config.json') as conf:
        config = json.load(conf)
        DATA_HOME = config['DATA_HOME']
        EX_HOME = sys.argv[1]
        SHEET = config['SHEET']
    COPORA = [os.path.join(DATA_HOME, corpus) for corpus in SHEET]

    # 데이터 체크, else 다운로드

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
    for i, corpus in enumerate(COPORA):
        with open(os.path.join(EX_HOME, 'tmp', 'process_'+str(i)+'.bin'), 'wb') as f:
            gen = make_gen(os.path.join(DATA_HOME, corpus))
            for line in gen:
                pickle.dump(line, f)

if __name__ == '__main__':
    main()