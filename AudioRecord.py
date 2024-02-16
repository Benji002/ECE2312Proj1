import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import numpy as np

# Define Sampling Rate or Frequency in Hz
sr = 44100

# Record duration in seconds
duration = 5
# Start audio recording
recording = sd.rec(int(duration*sr), samplerate=sr, channels=2) # we will record with a  mono or stereo channel microphone

# Record audio for the given duration
print("recording...............")
sd.wait()

# Write it to a file
write("sound4.wav",sr,recording)
# Look at the discrete number array we got from the audio
y, sr = librosa.load('sound4.wav')
fig, ax = plt.subplots(nrows=1, sharex=True)
print("recording shape", y.shape)
print("sampling rate", sr)
plt.figure(num=1,figsize=(7, 2.5))
librosa.display.waveshow(y=y, sr=sr,x_axis='time',color="blue")
plt.show()
ipd.Audio(y, rate=sr)