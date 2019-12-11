import os
from glob import glob
import requests
import json

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern), recursive=True)

def enroll(filename, speakerid):
    print(speakerid)
    url = 'http://aidemo.kuaishang.cn:9090/kst/enroll'
    d = {'spkid': speakerid,
        'node': 'dunyin',
        'wavtype': 'wav',
        'channel':'0',
        'type':'ti',
        'replaydetect':'true'}
    f = {'file':open(filename, 'rb')}
    r = requests.post(url, data=d, files=f)
    results = json.loads(r.text)
    print(results)
    flag = results['msg']
    return flag


# enroll dunyin people
directory = '/data/home/yezj/poc/dunyin/wav'
speakers_list = os.listdir(directory)
print('Find {0} speakers'.format(len(speakers_list)))

for ispeaker in speakers_list:
    idir = directory+'/'+ispeaker
    files = find_files(idir, pattern='*.wav')
    ifile = files[0]
    flag = enroll(ifile, ispeaker)
    if flag!=0:
        print('Fail {0}'.format(ispeaker))
    else:
        print('Success {0}'.format(ispeaker))

# enroll kst people
directory = '/data/yezj/icbc-data/kst-text-independent/16k'
speakers_list = os.listdir(directory)
print('Find {0} speakers'.format(len(speakers_list)))

for ispeaker in speakers_list:
    idir = directory+'/'+ispeaker
    ifile = idir+'/1_30.wav'
    flag = enroll(ifile, ispeaker)
    if flag!=0:
        print('Fail {0}'.format(ispeaker))
    else:
        print('Success {0}'.format(ispeaker))
