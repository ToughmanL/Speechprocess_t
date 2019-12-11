import os
from glob import glob
import numpy as np
from pyspeech import read_audio, write_audio
import shutil

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern))

directory = '/data/corpus/td-8k'
directory_save = '/data/yezj/Kst-text-dependent-8k/test'
files = find_files(directory, pattern='**/*.wav')
print('Find {0} files.'.format(len(files)))

speaker_list = {}
for ifile in files:
    ispeaker = ifile.split('/')[-2]
    if ispeaker not in speaker_list.keys():
        speaker_list[ispeaker] = [ifile]
    else:
        speaker_list[ispeaker].append(ifile)

for ispeaker in speaker_list.keys():
    sfiles = speaker_list[ispeaker]
    audio = []
    for ii in range(len(sfiles)):
        print(ii)
        ifile = sfiles[ii]
        if ii<3:
            audio.extend(list(np.squeeze(read_audio(ifile, 8000))))
        elif ii==3:
            ifile_dst = directory_save+'/enroll/'+ispeaker+'/1.wav'
            if os.path.exists(os.path.dirname(ifile_dst)) is False:
                os.makedirs(os.path.dirname(ifile_dst))
            print(len(audio))
            write_audio(np.array(audio), ifile_dst, sample_rate=8000)
            print('OK')
            ifile = sfiles[ii]
            ifile_dst = directory_save+'/verify/'+ispeaker+'/'+ifile.split('/')[-1]
            if os.path.exists(os.path.dirname(ifile_dst)) is False:
                os.makedirs(os.path.dirname(ifile_dst))
            shutil.copy(ifile, ifile_dst)
        else:
            ifile = sfiles[ii]
            ifile_dst = directory_save+'/verify/'+ispeaker+'/'+ifile.split('/')[-1]
            if os.path.exists(os.path.dirname(ifile_dst)) is False:
                os.makedirs(os.path.dirname(ifile_dst))
            shutil.copy(ifile, ifile_dst)
    print('Done {0}.'.format(ispeaker))


