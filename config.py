import os
import json
import sys
import logging
import logging.handlers
from collections import OrderedDict

# Make Configuration File


def main():
    experiment = int(sys.argv[1])
    config_file = 'config_ex0' + str(experiment) + '.json'

    if not os.path.exists(os.path.join(os.getcwd(), config_file)):
        print('Configuration not Detected, Creating...')
    else:
        print('Deleting Previous Configuration')
        os.remove(os.path.join(os.getcwd(), config_file))

    print('Input Blank if You Want to Edit Configuration Later.')
    config = OrderedDict()

    if experiment == 1:  # EX_01
        ex_path = input('Import Path To Save Experiment Data : ').replace('~', os.path.expanduser('~'))
        config["EX_HOME"] = ex_path  # ex/path_ex01?
        data_path = input('Import Path To Read/Download Corpus: ').replace('~', os.path.expanduser('~'))
        config["DATA_HOME"] = data_path
        sheet = [input('Import Path To Read Copora No.' + str(i) + ' (Op. Path): ') for i in range(5)]
        config["SHEET"] = sheet
        target = [input('Import Word To Do Expe. No.' + str(i) + ': ') for i in range(5)]
        config["TARGET"] = target

    elif experiment == 2:
        pass

    elif experiment == 3:
        pass

    else:
        # TODO: Raise Err
        pass

    logger = logging.getLogger(__name__)
    log_file = os.path.join(ex_path, 'ex0' + str(experiment), 'ex_log.log')
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
    filehandler = logging.FileHandler(log_file)
    logger.addHandler(filehandler)
    logger.setLevel(level=logging.DEBUG)

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')

    logger.debug('Configuration File Created')

