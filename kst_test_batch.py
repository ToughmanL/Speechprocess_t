import os
import requests
from glob import glob
import json
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import threading

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern), recursive=True)

#----------------------------------------url---------------------
#16k-ti
url_16k_ti_enroll = 'http://aidemo.kuaishang.cn:9080/kst/enroll'
url_16k_ti_verify = 'http://aidemo.kuaishang.cn:9080/kst/verify'
url_16k_ti_identify = 'http://aidemo.kuaishang.cn:9080/kst/identify'
#16k-td
url_16k_td_enroll = 'http://aidemo.kuaishang.cn:9080/kst/enroll'
url_16k_td_verify = 'http://aidemo.kuaishang.cn:9080/kst/verify'
url_16k_td_identify = 'http://aidemo.kuaishang.cn:9080/kst/identify'
#16k-rd
url_16k_rd_upload = 'http://aidemo.kuaishang.cn:9080/kst/rd/upload' 
url_16k_rd_enroll = 'http://aidemo.kuaishang.cn:9080/kst/rd/enroll'
url_16k_rd_verify = 'http://aidemo.kuaishang.cn:9080/kst/rd/verify'
url_16k_rd_identify = 'http://aidemo.kuaishang.cn:9080/kst/rd/identify'

#8k-ti
url_8k_ti_enroll = 'http://119.3.37.112:9070/kst/enroll'
url_8k_ti_verify = 'http://119.3.37.112:9070/kst/verify'
url_8k_ti_identify = 'http://119.3.37.112:9070/kst/identify'
#8k-td
url_8k_td_enroll = 'http://119.3.37.112:9070/kst/enroll'
url_8k_td_verify = 'http://119.3.37.112:9070/kst/verify'
url_8k_td_identify = 'http://119.3.37.112:9070/kst/identify'
#8k-rd
url_8k_rd_upload = 'http://119.3.37.112:9070/kst/rd/upload' 
url_8k_rd_enroll = 'http://119.3.37.112:9070/kst/rd/enroll'
url_8k_rd_verify = 'http://119.3.37.112:9070/kst/rd/verify'
url_8k_rd_identify = 'http://119.3.37.112:9070/kst/rd/identify'

node = 'cmblc'
num_workers =8
#---------------------------------------------------------------------------------
#-------------------------手机安静注册-手机安静辨认------------------------------------
#--------------------------------------------------------------------------------
#-------------------------网络信道16k-rd注册(安静）------------------------------------
'''
def rdEnroll_16k(files, node, spkid):
    for ii in range(len(files)):
        ifile = files[ii]
        param = {'node':node,
                'wavtype':'wav',
                'channel':'0',
                'spkid':spkid,
                'step':str(ii+1),
                'replaydetect':'false',
                'asrdetect':'false'}
        file = {'file': open(ifile,'rb')}
        reponse = requests.post(url=url_16k_rd_upload, data=param, files=file)
        results = json.loads(reponse.text)
        if results['code']==0:
            print('{0} upload succeed'.format(ifile))
        else:
            print('\033[1;35m {0} upload failure \033[0m'.format(ifile))
    param = {'node': node,
             'spkid':spkid}
    reponse = requests.post(url=url_16k_rd_enroll, data=param, files=file)
    results = json.loads(reponse.text)
    if results['code']==0:
        print('{0} enroll succeed'.format(spkid))
    else:
        print('\033[1;35m {0} enroll failure \033[0m'.format(spkid))

directory = '/data/home/yezj/poc/cmb-second/cmb-data/enroll/app-quiet-rd-5'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))

executor = ThreadPoolExecutor(max_workers=num_workers)
task = []
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        t = executor.submit(rdEnroll_16k, files, node, ispeaker)
        task.append(t)
    except:
        continue
wait(task, return_when=ALL_COMPLETED)
'''

#------------------------网络信道16k-rd辨认（安静）-----------------------

def rdIdentify_16k(filename, node, spkid, fileanme_save):
    param = {'node':node,
            'wavtype':'wav',
            'channel':'0',
            'topn':'1000',
            'replaydetect':'false',
            'asrdetect':'false'}
    file = {'file': open(filename,'rb')}
    reponse = requests.post(url=url_16k_rd_identify, data=param, files=file)
    results = json.loads(reponse.text)
    candidates = results['candidates']
    mutex.acquire(10)
    with open(filename_save,'a') as fw:
        for icandi in candidates:
            jspeaker = icandi['spkid']
            score = icandi['score']
            fw.write(jspeaker+' '+spkid+' '+str(score)+'\n')
    fw.close()
    mutex.release()
    print('{0} identify succeed.'.format(spkid))
'''
directory = '/data/home/yezj/poc/cmb-second/cmb-data/verify/app-quiet-rd-20'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
filename_save = 'scores_16k_rd_quiet.txt'

executor = ThreadPoolExecutor(max_workers=num_workers)
mutex = threading.Lock()
task = []
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        for ifile in files:
            t = executor.submit(rdIdentify_16k, ifile, node, ispeaker, filename_save)
            task.append(t)
    except:
        print('\033[1;35m {0} identify failure \033[0m'.format(ispeaker))
        continue
wait(task, return_when=ALL_COMPLETED)
'''
#---------------------------------------------------------------------------------
#-------------------------手机安静注册-手机嘈杂辨认------------------------------------
#--------------------------------------------------------------------------------

#------------------------网络信道16k-rd辨认（嘈杂）-----------------------
'''
directory = '/data/home/yezj/poc/cmb-second/cmb-data/verify/app-noise-rd-10-enhance'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
filename_save = 'scores_16k_rd_noise.txt'

executor = ThreadPoolExecutor(max_workers=num_workers)
mutex = threading.Lock()
task = []
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        print('Find {0} files'.format(len(files)))
        for ifile in files:
            t = executor.submit(rdIdentify_16k, ifile, node, ispeaker, filename_save)
            task.append(t)
    except:
        print('\033[1;35m {0} identify failure \033[0m'.format(ispeaker))
        continue
wait(task, return_when=ALL_COMPLETED)
'''

#---------------------------------------------------------------------------------
#-------------------------电话安静注册-电话安静辨认-ti------------------------------------
#--------------------------------------------------------------------------------
#-------------------------电话信道8k-ti注册(安静）------------------------------------
'''
def tiEnroll_8k(filename, node, spkid):
    param = {'node':node,
            'wavtype':'wav',
            'channel':'0',
            'spkid':spkid,
            'type':'ti',
            'replaydetect':'false',
            'asrdetect':'false'}
    file = {'file': open(filename,'rb')}
    reponse = requests.post(url=url_8k_ti_enroll, data=param, files=file)
    results = json.loads(reponse.text)
    print(results)
    if results['code']==0:
        print('{0} enroll succeed'.format(spkid))
    else:
        print('\033[1;35m {0} enroll failure \033[0m'.format(spkid))

directory = '/data/home/yezj/poc/cmb-second/cmb-data/enroll/phone-quiet-ti-1/'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
executor = ThreadPoolExecutor(max_workers=num_workers)
task = []
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        print('Find {0} files'.format(len(files)))
        filename = files[0]
        t = executor.submit(tiEnroll_8k, filename, node, ispeaker)
        task.append(t)
    except:
        continue
wait(task, return_when=ALL_COMPLETED)
'''
#-------------------------电话信道8k-ti辨认（安静）-----------------------
def tiIdentify_8k(filename, node, spkid, fileanme_save):
    param = {'node':node,
            'wavtype':'wav',
            'channel':'0',
            'topn':'1000',
            'type':'ti',
            'replaydetect':'false',
            'asrdetect':'false'}
    file = {'file': open(filename,'rb')}
    reponse = requests.post(url=url_8k_ti_identify, data=param, files=file)
    results = json.loads(reponse.text)
    candidates = results['candidates']
    mutex.acquire(10)
    with open(fileanme_save, 'a') as fw:
        for icandi in candidates:
            jspeaker = icandi['spkid']
            score = icandi['score']
            fw.write(jspeaker+' '+filename.split('/')[-1][:-4]+' '+str(score)+'\n')
    fw.close()
    mutex.release()
    print('{0} identify succeed.'.format(spkid))

directory = '/data/home/yezj/poc/cmb-second/cmb-data/verify/phone-quiet-ti-10'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
executor = ThreadPoolExecutor(max_workers=num_workers)
task = []
mutex = threading.Lock()
filename_save = 'scores_8k_ti_quiet.txt'
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        print('Find {0} files'.format(len(files)))
        for ifile in files:
            t = executor.submit(tiIdentify_8k, ifile, node, ispeaker, filename_save)
            task.append(t)
    except:
        print('\033[1;35m {0} identify failure \033[0m'.format(ispeaker))
        continue
wait(task, return_when=ALL_COMPLETED)

#---------------------------------------------------------------------------------
#-------------------------电话安静注册-手机安静辨认-ti------------------------------------
#--------------------------------------------------------------------------------

#-------------------------网络信道8k-ti辨认（安静）-----------------------
'''
directory = '/data/home/yezj/poc/cmb-second/cmb-data/verify/app-quiet-rd-20'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
executor = ThreadPoolExecutor(max_workers=num_workers)
task = []
mutex = threading.Lock()
filename_save = 'scores_8k_ti_16k_rd_quiet.txt'
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        print('Find {0} files'.format(len(files)))
        for ifile in files:
            t = executor.submit(tiIdentify_8k, ifile, node, ispeaker, filename_save)
            task.append(t)
    except:
        print('\033[1;35m {0} identify failure \033[0m'.format(ispeaker))
        continue
wait(task, return_when=ALL_COMPLETED)
'''
#---------------------------------------------------------------------------------
#-------------------------电话安静注册-手机嘈杂辨认-ti------------------------------------
#--------------------------------------------------------------------------------

#-------------------------网络信道8k-ti辨认（嘈杂）-----------------------
'''
directory = '/data/home/yezj/poc/cmb-second/cmb-data/verify/app-noise-rd-10'
speakers_list = os.listdir(directory)
print('Find {0} speakers.'.format(len(speakers_list)))
executor = ThreadPoolExecutor(max_workers=num_workers)
task = []
mutex = threading.Lock()
filename_save = 'scores_8k_ti_16k_rd_noise.txt'
for ispeaker in speakers_list:
    try:
        idir = directory+'/'+ispeaker+'/'
        files = find_files(idir, pattern='*.wav')
        print('Find {0} files.'.format(len(files)))
        for ifile in files:
            t = executor.submit(tiIdentify_8k, ifile, node, ispeaker, filename_save)
            task.append(t)
    except:
        print('\033[1;35m {0} identify failure \033[0m'.format(ispeaker))
        continue
wait(task, return_when=ALL_COMPLETED)
'''



