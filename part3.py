import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import numpy as np


#Loads the sound file in stereo
y_stereo, sr = librosa.load('sound3.wav', mono = False)

#Creates a shift and apends the right channel to it
#shift len of 11 for avg head 22 for 1ms 221 for 10ms and 2205 for 100ms
#shiftlen = 2205
#shift = np.zeros(shiftlen)
#shift = np.append(shift, y_stereo[0])
#print(sr)

#Copies the shifted audio to the left channel
#y_stereo[1] = shift[:-shiftlen].copy()
y_stereo[1] = y_stereo[0].copy()

#these print statements are just to check my work
#print(y_stereo[0][0])
#print(y_stereo[0][1])
#print(y_stereo[0][2])
#print(y_stereo[1][0])
#print(y_stereo[1][1])
#print(y_stereo[1][2])
write("BDodge_StereoSoundFile_0ms.wav",sr,y_stereo.T)