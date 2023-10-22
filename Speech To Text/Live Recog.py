import speech_recognition as sr
import sys
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import re

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

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

w1 = nlp(doc)
# Define a case-insensitive regex pattern as a string
# ans1 = r"(?i)integer pointer"
w2 = nlp("Integer Pointer")

answer1 = w1.similarity(w2)
print(answer1)
