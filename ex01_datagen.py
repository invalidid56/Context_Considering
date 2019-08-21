from konlpy.tag import Okt
import sys
import os
import pickle
import json

def main():
    # 로그 설정
    logger = logging.getLogger(__name__)
    log_file = os.path.join(ex_path, 'ex0' + str(experiment), 'ex_log.log')
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
    filehandler = logging.FileHandler(log_file)
    logger.addHandler(filehandler)
    logger.setLevel(level=logging.DEBUG)

    # 포스태거 인스턴스 생성
    tag = Okt()

    # 설정 파일 파싱
    with open('config_ex01.json') as conf:
        config = json.load(conf)
        DATA_HOME = config['DATA_HOME']
        EX_HOME = os.path.join(config['EX_HOME'], 'ex01')
        SHEET = config['SHEET']
    COPORA = [os.path.join(DATA_HOME, corpus) for corpus in SHEET]
    log.info('Reading Configuration')

    # TODO: 데이터 체크

    # 코퍼스 생성 함수 정의
    def make_gen(filedir):
        with open(os.path.join(DATA_HOME, filedir), 'rb') as f:
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
                    line = tag.morphs(line)
                    if not line == []:
                        yield line
                    else:
                        continue

    # 임시데이터 저장 디렉터리 생성
    os.makedirs(os.path.join(EX_HOME, 'tmp_data'))
    log.info('Tmpdir Created at '+EX_HOME+'/tmp_data')

    # 디렉터리에서 코퍼스 읽어서 임시데이터 생성
    for i, cor in enumerate(COPORA):
        corpus = os.listdir(cor)
        gens = [make_gen(os.path.join(DATA_HOME, cor, files)) for files in corpus]
        with open(os.path.join(EX_HOME, 'tmp', 'process_'+str(i))+'bin', 'wb') as f:
            for gen in gens:
                for line in gen:
                    pickle.dump(line, f)
            log.info('Temp File Created '+'process_'+str(i)+'.bin')

if __name__ == '__main__':
    main()
