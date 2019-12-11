import os
from glob import glob

def find_files(directory, pattern='**/*.wav'):
    return glob(os.path.join(directory, pattern), recursive=True)
    
directory = '/data/home/yezj/poc/bingjian/data'
directory_save = '/data/home/yezj/poc/bingjian/wav/enroll'
files = find_files(directory, pattern='*.wav')
print('Find {0} files.'.format(len(files)))
for ifile in files:
    file_zuoxi_left = directory_save+'/zuoxi/'+ifile.split('/')[-1].split('_')[1]+'/'+ifile.split('/')[-1]
    file_kehu_right = directory_save+'/kehu/'+ifile.split('/')[-1].split('_')[2]+'/'+ifile.split('/')[-1]
    if os.path.exists(os.path.dirname(file_zuoxi_left)) is False:
        os.makedirs(os.path.dirname(file_zuoxi_left))
    if os.path.exists(os.path.dirname(file_kehu_right)) is False:
        os.makedirs(os.path.dirname(file_kehu_right))
    cmd = 'ffmpeg -y -v \"quiet\"  -i '+ifile+' -ac 0 -filter_complex \"channelsplit[L][R]\" -map \"[L]\" -ac 1 -ar 8000 '+file_zuoxi_left+' -map \"[R]\"  -ac 1 -ar 8000 '+file_kehu_right
    os.popen(cmd)
    print('Done {0}'.format(ifile))