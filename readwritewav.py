# !usr/bin/env python
# coding=utf-8

import wave
import matplotlib.pyplot as plt
import numpy as np


def read_wave_data(file_path):
    # open a wave file, and return a Wave_read object
    f = wave.open(file_path, "rb")
    # read the wave's format infomation,and return a tuple
    params = f.getparams()
    # get the info
    # 读取格式信息
    # (声道数、量化位数、采样频率、采样点数、压缩类型、压缩类型的描述)
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    nchannels, sampwidth, framerate, nframes = params[:4]
    # Reads and returns nframes of audio, as a string of bytes.
    str_data = f.readframes(nframes)
    # close the stream
    f.close()
    # turn the wave's data to array
    wave_data = np.fromstring(str_data, dtype=np.short)
    # for the data is stereo,and format is LRLRLR...
    # shape the array to n*2(-1 means fit the y coordinate)
    wave_data.shape = -1, 2
    # transpose the data
    wave_data = wave_data.T
    # calculate the time bar
    time = np.arange(0, nframes) * (1.0 / framerate)
    return wave_data, time


def main():
    wave_data, time = read_wave_data("C:\Users\CJP\Desktop\miss_you.wav")
    # draw the wave
    plt.plot(time, wave_data[0])
    plt.show()

if __name__ == "__main__":
    main()


