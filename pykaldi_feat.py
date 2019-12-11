from kaldi.feat.mfcc import Mfcc, MfccOptions
from kaldi.feat.spectrogram import Spectrogram, SpectrogramOptions
from kaldi.matrix import SubVector, SubMatrix
from kaldi.util.options import ParseOptions
from kaldi.util.table import SequentialWaveReader
from kaldi.util.table import MatrixWriter
from numpy import mean
from sklearn.preprocessing import scale
import numpy as np
import pickle

def extract_mfcc(filename, samp_freq, frame_length_ms=25, frame_shift_ms=10,
                 num_ceps=23,                
                 round_to_power_of_two=True, snip_edges=True):
    '''
    extract mfcc using kaldi
    args:
        filename: wav file path
        samp_freq: sample frequence
    return:
        mfcc: (frame, fre)
    '''
    # get rspec and wspec
    with open('wav.scp','w') as f:
        f.write('test1 '+filename+'\n')
    rspec = 'scp,p:'+'wav.scp'
    wspec = 'ark,t:'+'spec.ark'
    # set po
    usage = """Extract MFCC features.Usage: example.py [opts...] <rspec> <wspec>"""
    po = ParseOptions(usage)
    po.register_float("min-duration", 0.0,"minimum segment duration")
    opts = po.parse_args()
    # set options
    mfcc_opts = MfccOptions()
    mfcc_opts.frame_opts.samp_freq = samp_freq
    mfcc_opts.num_ceps = num_ceps
    mfcc_opts.register(po)
    mfcc = Mfcc(mfcc_opts)
    sf = mfcc_opts.frame_opts.samp_freq
    with SequentialWaveReader(rspec) as reader, MatrixWriter(wspec) as writer:
        for key, wav in reader:
            if wav.duration < opts.min_duration:
                continue
            assert(wav.samp_freq >= sf)
            assert(wav.samp_freq % sf == 0)
            s = wav.data()
            s = s[:,::int(wav.samp_freq / sf)]
            m = SubVector(mean(s, axis=0))
            f = mfcc.compute_features(m, sf, 1.0)
            f_array = np.array(f)
            print(f_array.shape)
            writer[key] = f
    return f_array

def extract_spec(filename, samp_freq, frame_length_ms=25, frame_shift_ms=10,
                 round_to_power_of_two=True, snip_edges=True):
    '''
    extract spectrogram using kaldi
    args:
        filename: wav file path
        samp_freq: sample frequence
    return:
        spectrogram: (frame, fre)
    '''
    # get rspec and wspec
    with open('wav.scp','w') as f:
        f.write('test1 '+filename+'\n')
    rspec = 'scp,p:'+'wav.scp'
    wspec = 'ark,t:'+'spec.ark'
    # set po
    usage = """Extract MFCC features.Usage: example.py [opts...] <rspec> <wspec>"""
    po = ParseOptions(usage)
    po.register_float("min-duration", 0.0,"minimum segment duration")
    opts = po.parse_args()
    # set options
    spec_opts = SpectrogramOptions()
    spec_opts.frame_opts.samp_freq = samp_freq
    spec_opts.frame_opts.frame_length_ms = frame_length_ms
    spec_opts.frame_opts.frame_shift_ms = frame_shift_ms
    spec_opts.frame_opts.round_to_power_of_two = round_to_power_of_two
    spec_opts.frame_opts.snip_edges = snip_edges
    spec_opts.register(po)
    spec = Spectrogram(spec_opts)
    sf = spec_opts.frame_opts.samp_freq
    with SequentialWaveReader(rspec) as reader, MatrixWriter(wspec) as writer:
        for key, wav in reader:
            if wav.duration < opts.min_duration:
                continue
            assert(wav.samp_freq >= sf)
            assert(wav.samp_freq % sf == 0)
            s = wav.data()
            s = s[:,::int(wav.samp_freq / sf)]
            m = SubVector(mean(s, axis=0))
            f = spec.compute_features(m, sf, 1.0)
            f_array = np.array(f)
            writer[key] = f
    return f_array

if __name__=='__main__':
    filename = 'linlp02_01_01.wav'
    extract_mfcc(filename, samp_freq=16000, frame_length_ms=108, frame_shift_ms=12.5,
                 round_to_power_of_two=False, snip_edges=False)
