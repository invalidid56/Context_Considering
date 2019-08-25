import sys
import os
import random
import shutil


def main():
    print('Mixing Corpus: ')
    total = int(input('Input Count of Document to Put in Corpus: '))
    output = input('Input Directory To Make Corpus: ')


    sheet = []
    while True:
        doc = input('Input Directory of Original Corpus: ')
        rte = int(input('Input Rate to Apply: '))
        sheet.append((doc, rte))
        ext = input('Input P to Continue: ')
        if not ext.upper() == 'P':
            break

    result = []
    rt = sum([r[1] for r in sheet])
    for corpus in sheet:
        c = (corpus[1]/rt) * total
        filelist = os.listdir(corpus[0])
        filelist = random.shuffle(filelist)
        filelist = filelist[:c]
        filelist = [os.path.join(corpus[0], file) for file in filelist]
        result += filelist

    os.mkdirs(output)
    for file in result:
        shutil.copy(file, output)

    print('finished')