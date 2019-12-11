#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:16:05 2018
 
"""
 
import wave
import os
 
 
def is_wav(f):
    res = True
    try:
        wave.open(f)
    except wave.Error as e:
        res = False
    return res
 
 
def pcm2wav(pcm_file, save_file, channels=1, bits=16, sample_rate=8000):
    """ pcm转换为wav格式
        Args:
            pcm_file pcm文件
            save_file 保存文件
            channels 通道数
            bits 量化位数，即每个采样点占用的比特数
            sample_rate 采样频率
    """
    if is_wav(pcm_file):
        raise ValueError('"' + str(pcm_file) + '"' +
                         " is a wav file, not pcm file! ")
 
    pcmf = open(pcm_file, 'rb')
    pcmdata = pcmf.read()
    pcmf.close()
 
    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))
 
    wavfile = wave.open(save_file, 'wb')
 
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
 
    wavfile.writeframes(pcmdata)
    wavfile.close()
 
 
def convert_dir(root, ext=".pcm", **kwargs):
    """ 把一个文件夹内的pcm，统统加上头
        Args:
            root 文件夹根目录
            ext pcm文件的扩展名
    """
 
    from tqdm import tqdm
 
    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(root)
                 for f in files
                 if os.path.splitext(f)[1] == ext]
 
    for src_file in tqdm(src_files, ascii=True):
        try:
            wav_file = os.path.splitext(src_file)[0] + ".wav"
            pcm2wav(src_file, wav_file, **kwargs)
        except Exception as e:
            print('Convert fail: ' + src_file)
            print(e)
 
 
if __name__ == '__main__':
    # pcm = r'1.pcm'
    # wav = pcm[:-4] + '.wav'
    # pcm2wav(pcm, wav)
    convert_dir('/data/corpus/aurora/test_mrd_cF/test_mrd_cF', '.pcm')
