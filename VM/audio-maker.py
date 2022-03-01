# STT
import speech_recognition as sr 
# TTS
from gtts import gTTS
import pygame
#Translate
from deep_translator import GoogleTranslator

TEXT ='시작.'
language_toSay='ko'

myobj = gTTS(text=TEXT, lang=language_toSay, slow=False)
myobj.save("./start.mp3")

pygame.mixer.init()
pygame.mixer.music.load("./start.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue