# check config.json, check setup.py

import os
import json
from collections import OrderedDict

# Config.json
if not os.path.exists(os.path.join(os.getcwd(), 'config.json')):
    print('config.json not detected,')
    ex_path = input('Import Path To Save Experiment Data : ').replace('~', os.path.expanduser('~'))
    data_path = input('Import Path To Read/Download Corpus: ').replace('~', os.path.expanduser('~'))
    sheet = [input('Import Path To Read Copora No.'+ str(i) +' (Op. Path): ') for i in range(5)]
    for path in [ex_path, data_path]:
        if not os.path.isdir(path):
            os.makedirs(path)


    config = OrderedDict()
    config["EX_HOME"] = ex_path
    config["DATA_HOME"] = data_path
    config["SHEET"] = sheet

    with open('config.json', 'w',  encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent='\t')


# TODO: Check Package Dependency