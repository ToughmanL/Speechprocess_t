file_read = 'plda_scores'
fr = open(file_read, 'r')
line = fr.readline()
fw = open('high.txt','w')
while line:
    linesp = line.split('\n')[0].split(' ')
    file1 = linesp[0]
    file2 = linesp[1]
    isim = float(linesp[2])
    if file1.split('/')[-2]==file2.split('/')[-2] and isim<1000:
        fw.write(file1+' '+file2+' '+str(isim)+'\n')
    line = fr.readline()
fr.close()
fw.close()
