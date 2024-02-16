import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import numpy as np

y_stereo, sr = librosa.load('BDodge_StereoSoundFile_AVGHead.wav', mono = False)

#I calculated the scallar attenuation value by doing 10^(dB/10)
# -1.5dB = 0.71 -3dB = 0.5 -6dB = 0.25
att = 0.71
y_stereo[1] = y_stereo[1]*att

print(y_stereo[0][0])
print(y_stereo[0][1])
print(y_stereo[0][2])
print(y_stereo[1][0])
print(y_stereo[1][1])
print(y_stereo[1][2])

write("BDodge_StereoSoundFile_AVGHead_-1.5dB.wav",sr,y_stereo.T)
