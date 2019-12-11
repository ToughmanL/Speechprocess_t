file_read = 'plda_scores'
fr = open(file_read, 'r')
line = fr.readline()
fw = open('trials.txt','w')
while line:
    linesp = line.split('\n')[0].split(' ')
    file1 = linesp[0]
    file2 = linesp[1]
    if file1.split('/')[-2]==file2.split('/')[-2]:
        target='target'
    else:
        target='nontarget'
    fw.write(file1+' '+file2+' '+target+'\n')
    line = fr.readline()
fr.close()
fw.close()
