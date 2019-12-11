import os
from glob import glob
from pyspeech import read_audio, vad

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern), recursive=True)

directory = '/data/home/yezj/poc/bingjian/wav/verify/kehu'
file_save = 'verify_len.txt'
files = find_files(directory, pattern='**/*.wav')
print('Find {0} filses.'.format(len(files)))
fw = open(file_save, 'w')
for ifile in files:
        print(ifile)
        audio = read_audio(ifile, 8000)
        audio = vad(audio, 8000)
        len_audio = len(audio)/8000
        fw.write(ifile+' '+str(len_audio)+'\n')
        print('Done {0}\n'.format(ifile))
    #except:
    #    continue
fw.close()