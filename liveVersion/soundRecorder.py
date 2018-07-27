import pyaudio
import wave
from scipy.io import wavfile as wav


class soundRecorder:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    def record(self, RECORD_SECONDS):
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            frames.append(data)
# not efficientbut wav normalizes the data for me, can change if extremely slow
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT)*2)
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        rate, dataSound = wav.read('output.wav')
        dataSound = dataSound/100000
        return dataSound
