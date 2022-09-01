from fileinput import filename
import sounddevice
from scipy.io.wavfile import write


def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec(
        (seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")
    #filename = input('Enter File name and extension (e.g .wav, .mp3): ')


voice_recorder(15, 'filename.mp3')
