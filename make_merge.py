import os
from glob import glob
import numpy as np
from pyspeech import read_audio, write_audio
import shutil

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern))

directory = '/data/home/yezj/wav-tool/data_demo/data_demo/train'
directory_save = '/data/home/yezj/wav-tool/data_demo/data_demo/train-one'
sample_rate = 16000

speakers_list = os.listdir(directory)
print('Find {0} speakers'.format(len(speakers_list)))

for ispeaker in speakers_list:
    idir = directory+'/'+ispeaker
    files = find_files(idir, pattern='*.wav')
    audio = []
    for ifile in files:
        try:
            iaudio = read_audio(ifile, sample_rate)
        except:
            continue
        audio.extend(list(np.squeeze(iaudio)))
        ifile_dst = directory_save+'/'+ispeaker+'/1.wav'
        if os.path.exists(os.path.dirname(ifile_dst)) is False:
            os.makedirs(os.path.dirname(ifile_dst))
    write_audio(np.array(audio), ifile_dst, sample_rate=sample_rate)
    print('Done {0}.'.format(ispeaker))


        
