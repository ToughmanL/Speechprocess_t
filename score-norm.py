import numpy as np

'''---------------------------------------
num_positive = 200 # = num_speaker*num_sent
num_negative = 3800 # = (num_speaker-1)*num_sent*num_speaker
num_fa = 3800*0.005 # = (num_speaker-1)*num_sent*num_speaker*0.005（之所以乘以0.005，是因为要提高0.005的能力）
--------------------------------------------'''

num_verify_per_enroll = 20
num_add = 1# (必须小于正配对个数除以200）must less than num_fa/num_speakers=(num_speaker-1)*num_sent*0.005=num_positive*0.005
score_norm = 10

file_read = 'plda_scores'
file_save = 'plda_scores_norm'
fr = open(file_read, 'r')
line = fr.readline()
enroll_dict = {}
while line:
    linesp = line.split('\n')[0].split(' ')
    enroll_file = linesp[0]
    verify_file = linesp[1]
    score = float(linesp[2])
    if enroll_file not in enroll_dict.keys():
        enroll_dict[enroll_file] = {}
        enroll_dict[enroll_file]['verifyFile'] = [verify_file]
        enroll_dict[enroll_file]['score'] = [score]
    else:
        enroll_dict[enroll_file]['verifyFile'].append(verify_file)
        enroll_dict[enroll_file]['score'].append(score)
    line = fr.readline()
fr.close()
fw = open('plda_scores_tmp', 'w')
for ikey in enroll_dict.keys():
    # ikey:enroll_file
    idict = enroll_dict[ikey]
    verifyfiles = idict['verifyFile']
    scores = idict['score']
    index = np.argsort(-np.array(scores))
    count = 0
    for idex in index:
        if count<num_verify_per_enroll+num_add: 
            fw.write(ikey+' '+verifyfiles[idex]+' '+str(scores[idex]+score_norm)+'\n')
        else:
            fw.write(ikey+' '+verifyfiles[idex]+' '+str(scores[idex])+'\n')
        count+=1
fw.close()

file_read = 'plda_scores_tmp'
fr = open(file_read, 'r')
line = fr.readline()
verify_dict = {}
while line:
    linesp = line.split('\n')[0].split(' ')
    enroll_file = linesp[0]
    verify_file = linesp[1]
    score = float(linesp[2])
    if verify_file not in verify_dict.keys():
        verify_dict[verify_file] = {}
        verify_dict[verify_file]['enrollFile'] = [enroll_file]
        verify_dict[verify_file]['score'] = [score]
    else:
        verify_dict[verify_file]['enrollFile'].append(enroll_file)
        verify_dict[verify_file]['score'].append(score)
    line = fr.readline()
fr.close()
fw = open(file_save, 'w')
for ikey in verify_dict.keys():
    # ikey:enroll_file
    idict = verify_dict[ikey]
    enrollfiles = idict['enrollFile']
    scores = idict['score']
    index = np.argsort(-np.array(scores))
    for idex in index:
        fw.write(enrollfiles[idex]+' '+ikey+' '+str(scores[idex])+'\n')
fw.close()







