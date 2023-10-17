import speech_recognition as sr
import sys

# filename = sys.argv[1]
filename = "Seen.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
if __name__ == '__main__':
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
