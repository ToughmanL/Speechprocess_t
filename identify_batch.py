import os
import requests
from glob import glob
import json
from concurrent.futures import ThreadPoolExecutor
import threading
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
def tiIdentify(filename, node, ispeaker):
    param = {'node':node,
             'wavtype':'wav',
             'channel':'0',
             'topn':'1000',
             'type':'ti',
             'replaydetect':'false',
             'asrdetect':'false'}
    file = {'file': open(filename,'rb')}
    reponse = requests.post(url=url_16k_ti_identify, data=param, files=file)
    results = json.loads(reponse.text)
    candidates = results['candidates']
    mutex.acquire(10)
    with open('scores_16k_ti_0228.txt','a') as f:
        for icandi in candidates:
            jspeaker = icandi['spkid']
            score = icandi['score']
            f.write(jspeaker+' '+ispeaker+' '+str(score)+'\n')
    mutex.release()
    print('{0} identify succeed.'.format(ispeaker))

executor = ThreadPoolExecutor(max_workers=10)
directory = 'data/gonghang_100ren/ti-16k'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
task = []
mutex = threading.Lock()
time_start = time.time()
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        if len(files)!=2:
            continue
        filename_enroll = files[0][:-6]+'15.wav'
        node = 'yezjvb'
        t = executor.submit(tiIdentify, filename_enroll, node, ispeaker)
        task.append(t)
    except:
        print('{0} failure failure failure'.format(filename_enroll))
        continue
time_end = time.time()
print('Using time {0}'.format(time_end-time_start))