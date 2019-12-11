import os
from glob import glob
import argparse

def find_files(directory, pattern='**/*.wav'):
    if len(directory)==1 or isinstance(directory,str):
        if len(directory)==1:
            directory = directory[0]
        return glob(os.path.join(directory, pattern), recursive=True)
    if len(directory)>1 and isinstance(directory,list):
        files_path=[]
        for ii in directory:
            files_path.extend(glob(os.path.join(ii, pattern), recursive=True))
        return files_path

def mp3towav(args):
    directory = args.directory
    pattern = args.pattern
    directory_save = args.directory_save
    if os.path.exists(directory_save) is False:
        os.makedirs(directory_save)
    files = find_files(directory, pattern=pattern)
    print('find {0} files'.format(len(files)))
    count = 0
    for ifile in files:
        ifile_dst = directory_save+'/'+ifile.split('/')[-4]+'/'+ifile.split('/')[-3]+'/'+ifile.split('/')[-2]+'/'+ifile.split('/')[-1][:-4]+'.wav'
        if os.path.exists(os.path.dirname(ifile_dst)) is False:
            os.makedirs(os.path.dirname(ifile_dst))
        try:
            os.popen('ffmpeg -y -v \"quiet\"  -i \"'+ifile+'\" -ar 16000 -ac 1 \"'+ifile_dst+ '\"')
        except:
            pass
        print('Done: {0} {1}'.format(count, len(files)))
        count+=1

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory',type=str, default='', help='Path to the mp3 directory')
    parser.add_argument('--directory_save',type=str, default='', help='Path to the wav directory')
    parser.add_argument('--pattern',type=str, default='*.mp3', help='pattern')
    args = parser.parse_args()
    mp3towav(args)

    
