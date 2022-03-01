# STT
import speech_recognition as sr 
# TTS
from gtts import gTTS
import os
import pygame
#translate
from deep_translator import GoogleTranslator

r = sr.Recognizer()
speech = sr.Microphone(device_index=1)

pygame.mixer.init()        
pygame.mixer.music.load("/home/pi/AI-speaker-toy-project/VM/start.mp3")
pygame.mixer.music.play()

while(True):

  with speech as source:
      print("say something!…")
      audio = r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      
  try:
      recog = r.recognize_google(audio, language = 'ko-KR') #en-US #ko-KR
      print("try1: " + recog)
      
      if(recog.find('지니')>=0): #시동어 인식 
      
        print("You said: " + recog)
        
        pygame.mixer.music.load("/home/pi/AI-speaker-toy-project/VM/yes-sir.mp3")
        pygame.mixer.music.play()
          
        while pygame.mixer.music.get_busy() == True:
           continue
        
        with speech as mysource:
          print("I heard 지니, say words!…")
          myaudio = r.adjust_for_ambient_noise(mysource)
          myaudio = r.listen(mysource)
        
        try: #시동어 인식 후 음성 재 인식
          myrecog = r.recognize_google(myaudio, language = 'ko-KR')
          print("You said after 지니: " + myrecog)

          translated = GoogleTranslator(source='auto', target='en').translate(myrecog)
          
          # TTS
          language_toSay='en'
          myobj = gTTS(text=translated, lang=language_toSay, slow=False)
          myobj.save("/home/pi/AI-speaker-toy-project/VM/TTS_file.mp3")
          
          pygame.mixer.music.load("/home/pi/AI-speaker-toy-project/VM/TTS_file.mp3")
          pygame.mixer.music.play()
          
          while pygame.mixer.music.get_busy() == True:
            continue
            
        except sr.UnknownValueError:
          print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))
          
  except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))


