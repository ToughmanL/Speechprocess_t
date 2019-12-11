import os
import wave
from glob import glob

def find_files(directory, pattern):
    return glob(os.path.join(directory, pattern))

def stoMono(src_file, dst_file_l, dst_file_r):
    f = wave.open(file1, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
 
    # 将波形数据转换为数组
    wave_data = np.fromstring(str_data, dtype=np.int16)
    wave_data.shape = -1, 2
    wave_data = wave_data.T

    wave_data_1 = wave_data[0]  # 声道1
    wave_data_2 = wave_data[1]  # 声道2

    w1 = wave_data_1.tostring()
    w2 = wave_data_2.tostring()
    
    with open(dst_file_l, 'wb') as fw:
        wf.setnchannels(1)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(w1)

    with open(dst_file_r, 'wb') as fw:
        wf.setnchannels(1)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(w2)

if __name__=='__name__':
    directory = ''
    directory_save = ''
    files = find_files(directory, pattern='*.wav')
    print('Find {0} files.'.format(len(files)))
    for ifile in files:
        ifile_dst_l = directory_save+'/'+ifile.split('/')[-1][:-4]+'_left.wav'
        if os.path.exists(os.path.dirname(ifile_dst_l)) is False:
            os.makedirs(os.path.dirname(ifile_dst_l))

        ifile_dst_r = directory_save+'/'+ifile.split('/')[-1][:-4]+'_right.wav'
        if os.path.exists(os.path.dirname(ifile_dst_r)) is False:
            os.makedirs(os.path.dirname(ifile_dst_r))

        stoMono(ifile, ifile_dst_l, ifile_dst_r)
        print('Done {0}'.format(ifile))
