# check config.json, check setup.py

import os
import json
from collections import OrderedDict

# Config.json
if not os.path.exists(os.path.join(os.getcwd(), 'config.json')):
    print('config.json not detected,')
    ex_path = input('Import Path To Save Experiment Data : ')
    data_path = input('Import Path To Read/Download Corpus: ')
    sheet_path = input('Import Path To Import Experiment Settings: ')

    config = OrderedDict()
    config["EX_HOME"] = ex_path
    config["DATA_HOME"] = data_path
    config["SHEET_HOME"] = sheet_path

    with open('config.json', 'w',  encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')


# TODO: Check Package Dependency