import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from initComputers import wake_on_lan

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
global command

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():  
  try:
    with sr.Microphone() as source:   
      listener.adjust_for_ambient_noise(source)
      print('listening...')
      voice = listener.listen(source)
      command = listener.recognize_google(voice, language='pt-BR')
      command = listener.recognize_google(command)
      command = command.lower()
      if 'Alexa' in command:
        command = command.replace('Alexa', '')
  except:# sr.UnknownValueError:    
    #talk('Não entendi, repita por favor.')
    #command = take_command()
    pass
  return command

def run_alexa():
  command = take_command()
  if 'toca' in command:
    song = command.replace('toca', '')
    talk('Tocando' + song)
    pywhatkit.playonyt(song)
  elif 'horas' in command:
    time = datetime.datetime.now().strftime('%H:%M')
    talk('Agora são exatamente ' + time)
  elif 'ligar pc' in command:
    talk('Ligando computador')
    wake_on_lan('0A-E0-AF-D2-20-23')


run_alexa()