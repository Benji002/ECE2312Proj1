import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import numpy as np


#I made my own audio recording of do re mi... to compare and then I ran this to make my own spectrogram
y, sr = librosa.load('sound3.wav')
fig, ax = plt.subplots(nrows=1, sharex=True)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
img = librosa.display.specshow(D, y_axis='linear', x_axis='time',sr=sr)
plt.show()