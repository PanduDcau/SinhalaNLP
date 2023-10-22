import speech_recognition as sr
import sys
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

duration = int(input("Duration of Microphone is Open :"));

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)

