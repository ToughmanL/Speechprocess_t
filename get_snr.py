import os
from glob import glob
from pyspeech import read_audio, vad, speech_enhance
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
ser = speech_enhance()
def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern), recursive=True)

directory = '/data/home/yezj/poc/bingjian/wav-16k/enroll/kehu'
file_save = 'enroll_snr.txt'
files = find_files(directory, pattern='**/*.wav')
print('Find {0} filses.'.format(len(files)))
fw = open(file_save, 'w')
for ifile in files:
        snr = ser.eval_snr_fast(ifile, 16000)
        fw.write(ifile+' '+str(snr)+'\n')
        print('Done {0}\n'.format(ifile))
    #except:
    #    continue
fw.close()