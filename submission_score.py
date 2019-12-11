import os
import numpy as np

def submission_score(trials, similarity, roc):

    fr_t = open(trials,'r')
    fr_s = open(similarity,'r')
    line_t = fr_t.readline()
    line_s = fr_s.readline()
    count = 0
    p_sim = []
    n_sim = []
    while line_t:
        line_t_sp = line_t.split('\n')[0].split(' ')
        file1 = line_t_sp[0]
        file2 = line_t_sp[1]
        target = line_t_sp[2]

        line_s_sp = line_s.split('\n')[0].split(' ')
        sim = float(line_s_sp[2])        
        count+=1
        line_t = fr_t.readline()
        line_s = fr_s.readline()

        if target=='target':
            p_sim.append(sim)
        elif target=='nontarget':
            n_sim.append(sim)

    p_sim = np.array(p_sim)
    n_sim = np.array(n_sim)
    fr_t.close()
    fr_s.close()

    num_threshold = 2100
    frr = np.zeros(num_threshold)
    far = np.zeros(num_threshold)
    count = 0
    #print(p_sim)
    print(len(p_sim))
    for isim in p_sim:
        if isim<-1400:
            print(isim)
    for threshold in np.linspace(-200, 200, num_threshold):
        num_frr = np.sum(np.int0(p_sim < threshold), axis=0)
        frr[count] = num_frr / len(p_sim)
        num_far = np.sum(np.int0(n_sim > threshold), axis=0)
        far[count] = num_far / len(n_sim)
        count = count + 1

    index_min = np.argmin(np.abs(frr - far), axis=0)
    eer = (frr[index_min] + far[index_min]) / 2
    thred = np.linspace(-200, 200, num_threshold)[index_min]
    #print(eer)
    #print(far)
    #print(frr)
    #print('eer:{0}, thred:{1}'.format(eer, thred))
    thred_range = np.linspace(-200, 200, num_threshold)
    fw = open(roc, 'w')
    flag_001 = 0
    flag_0005 = 0
    flag_0001 = 0
    flag_00001 = 0
    flag_000001 = 0
    for ii in range(num_threshold):
        if far[ii]<0.01 and flag_001==0:
            print('百分之一 {1} {2} (far: {0}, 1-frr:{1}, thred:{2})'.format(far[ii], 1-frr[ii], thred_range[ii]))
            flag_001 = 1
        if far[ii]<0.005 and flag_0005==0:
            print('千分之五 {1} {2} (far: {0}, 1-frr:{1}, thred:{2})'.format(far[ii], 1-frr[ii], thred_range[ii]))
            flag_0005 = 1
        if far[ii]<0.001 and flag_0001==0:
            print('千分之一 {1} {2} (far: {0}, 1-frr:{1}, thred:{2})'.format(far[ii], 1-frr[ii], thred_range[ii]))
            flag_0001 = 1
        if far[ii]<0.0001 and flag_00001==0:
            print('万分之一 {1} {2} (far: {0}, 1-frr:{1}, thred:{2})'.format(far[ii], 1-frr[ii], thred_range[ii]))
            flag_00001 = 1
        if far[ii]<0.00001 and flag_000001==0:
            print('十万分之一 {1} {2} (far: {0}, 1-frr:{1}, thred:{2})'.format(far[ii], 1-frr[ii], thred_range[ii]))
            flag_000001 = 1

        fw.write(str(thred_range[ii])+' '+str(far[ii])+' '+str(frr[ii])+'\n')
    print('eer:{0}, thred:{1}'.format(eer, thred))
    fw.close()

if __name__=='__main__':
    trials = 'trials.txt'
    similarity = 'plda_scores'
    roc = 'roc.txt'
    submission_score(trials, similarity, roc)

