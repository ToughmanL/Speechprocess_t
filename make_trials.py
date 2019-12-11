import os
from glob import glob
import numpy as np
from pyspeech import read_audio, write_audio
import shutil

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern))

directory_enroll = '/data/yezj/Kst-text-dependent-8k/test/enroll'
file_enroll = find_files(directory_enroll, pattern='**/*.wav')
print('Find {0} enroll files.'.format(len(file_enroll)))

directory_verify = '/data/yezj/Kst-text-dependent-8k/test/verify'
file_verify = find_files(directory_verify, pattern='**/*.wav')
print('Find {0} verify files.'.format(len(file_verify)))

fw = open('trials.txt','w')
for ifile in file_enroll:
    for jfile in file_verify:
        if ifile.split('/')[-2] == jfile.split('/')[-2]:
            target = 'target'
        else:
            target = 'nontarget'
        fw.write(ifile+' '+jfile+' '+target+'\n')
fw.close()
