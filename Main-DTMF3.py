import numpy as np
import pyaudio
import DTMF2

CHUNK = 16000
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, frames_per_buffer=CHUNK)

while True:
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    print(data)
    new_res = DTMF2.DTMF(data, RATE)
    if new_res != "":
        print(new_res)
    # player.write(data, CHUNK)
