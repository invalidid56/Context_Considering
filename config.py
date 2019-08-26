import os
import json
import sys
import logging
import logging.handlers
from collections import OrderedDict


def main():
    experiment = int(sys.argv[1])
    config_file = 'config_ex0' + str(experiment) + '.json'
    project_name = {
        1: 'ex01_wv_visualize_cluster',
        2: 'ex02_document_cluster',
        3: 'ex03_attention_classifier'
    }

    if not os.path.exists(os.path.join(os.getcwd(), project_name[experiment], config_file)):
        print('Configuration not Detected, Creating...')
    else:
        print('Deleting Previous Configuration')
        os.remove(os.path.join(os.getcwd(), project_name[experiment], config_file))

    print('Input Blank if You Want to Edit Configuration Later.')
    config = OrderedDict()

    if experiment == 1:  # EX_01
        ex_path = input('Import Path To Save Experiment Data : ').replace('~', os.path.expanduser('~'))
        config["EX_HOME"] = ex_path
        data_path = input('Import Path To Read/Download Corpus: ').replace('~', os.path.expanduser('~'))
        config["DATA_HOME"] = data_path
        sheet = [input('Import Path To Read Copora No.' + str(i) + ' (Op. Path): ') for i in range(5)]
        config["SHEET"] = sheet
        target = [input('Import Word To Do Expe. No.' + str(i) + ': ') for i in range(5)]
        config["TARGET"] = target

    elif experiment == 2:
        ex_path = input('Import Path To Save Experiment Data : ').replace('~', os.path.expanduser('~'))
        config["EX_HOME"] = ex_path
        config["DATA_HOME"] = input('Import Path To Read/Download Corpus: ').replace('~', os.path.expanduser('~'))
        config["CLUSTER"] = input('Import Number of Clusters to Make :')
        sheet = [input('Import Path To Read Copora No.' + str(i) + ' (Op. Path): ') for i in range(2)]
        config["SHEET"] = sheet

    elif experiment == 3:
        ex_path = input('Import Path To Save Experiment Data : ').replace('~', os.path.expanduser('~'))
        config["EX_HOME"] = ex_path
        config["DATA_HOME"] = input('Import Path To Read/Download Corpus: ').replace('~', os.path.expanduser('~'))
    else:
        # TODO: Raise Err
        pass

    logger = logging.getLogger(__name__)
    log_file = os.path.join(ex_path, 'ex0' + str(experiment), 'ex_log.log')
    os.makedirs(os.path.join(ex_path, 'ex0'+str(experiment)))
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
    filehandler = logging.FileHandler(log_file)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(level=logging.DEBUG)

    with open(os.path.join(os.getcwd(), project_name[experiment], config_file), 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')

    logger.debug('Configuration File Created')


if __name__ == '__main__':
    main()