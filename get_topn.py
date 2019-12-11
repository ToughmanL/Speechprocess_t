import numpy as np
file_read = 'plda_scores'
fr = open(file_read, 'r')
line = fr.readline()
verify_scores = {}
while line:
    linesp = line.split('\n')[0].split(' ')
    speakerid = linesp[0].split('/')[-2]
    verify_uttid = linesp[1].split('/')[-1]
    isim = float(linesp[2])
    if verify_uttid not in verify_scores.keys():
        verify_scores[verify_uttid] = {}
        verify_scores[verify_uttid]['speakerid'] = []
        verify_scores[verify_uttid]['speakerid'].append(speakerid)
        verify_scores[verify_uttid]['score'] = []
        verify_scores[verify_uttid]['score'].append(isim)
    else:
        verify_scores[verify_uttid]['speakerid'].append(speakerid)
        verify_scores[verify_uttid]['score'].append(isim)

    line = fr.readline()
fr.close()

fw = open('top2.txt','w')
for uttid in verify_scores.keys():
    speakerid_list = np.array(verify_scores[uttid]['speakerid'])
    scores_list = np.array(verify_scores[uttid]['score'])
    index_max = np.argsort(-scores_list)
    for ii in range(2):
        index = index_max[ii]
        iscore = scores_list[index]
        ispeaker = speakerid_list[index]
        fw.write(uttid+' '+ispeaker+' '+str(iscore)+'\n')
fw.close()

