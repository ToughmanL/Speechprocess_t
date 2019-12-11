import os
import requests
from glob import glob
import json
from concurrent.futures import ThreadPoolExecutor
import time

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern), recursive=True)

#----------------------------------------url---------------------
#16k-ti
url_16k_ti_enroll = 'http://10.0.2.124:9060/kst/enroll'
url_16k_ti_verify = 'http://10.0.2.124:9060/kst/verify'
url_16k_ti_identify = 'http://10.0.2.124:9060/kst/identify'

#------------------------ti-----------------------------------#
#http://aidemo.kuaishang.cn:9080/kst/enroll?node=icbc&wavtype=wav&channel=0&spkid=56789&type=ti&replaydetect=true&asrdetect=false&text=您好中国工商银行
def tiEnroll(filename,node,spkid):
    param = {'node':node,
             'wavtype':'wav',
             'channel':'0',
             'spkid':spkid,
             'type':'ti',
             'replaydetect':'false',
             'asrdetect':'false'}
    file = {'file': open(filename,'rb')}
    reponse = requests.post(url=url_16k_ti_enroll, data=param, files=file)
    results = json.loads(reponse.text)
    if results['code']==0:
        print('{0} enroll succeed'.format(spkid))
    else:
        print('{0} enroll failure failure failure'.format(spkid))

executor = ThreadPoolExecutor(max_workers=10)
directory = 'data/gonghang_100ren/ti-16k'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
task = []
time_start = time.time()
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        if len(files)!=2:
            continue
        filename_enroll = files[0][:-6]+'30.wav'
        node = 'yezjbn'
        t = executor.submit(tiEnroll, filename_enroll, node, ispeaker)
        task.append(t)
    except:
        print('{0} upload failure failure failure'.format(filename_enroll))
        continue
time_end = time.time()
print('Using time {0}'.format(time_end-time_start))