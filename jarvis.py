import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Roger and Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from user and returns string as output

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:,{query}\n")
    except Exception as e:
        print(e)

        print("Please say again")
        return "None"
    return query

if __name__=="__main__":
  wishMe()
  while True:
  if 1:
    query= takeCommand().lower()

  #logic for executing tasks based on query
  if 'wikipedia' in query:
      speak('Searching wikipedia...')
      query = query.replace("wikipedia","")
      results= wikipedia.summary(query,sentences=3)
      speak("According to wikipedia")
      print(results)
      speak(results)

  elif 'open youtube' in query:
      webbrowser.open("youtube.com")
  elif 'open google' in query:
      webbrowser.open("google.com")
  elif 'open stackoverflow' in query:
      webbrowser.open('stackoverflow.com')  
  elif 'the time' in query:
      strTime= datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir,the time is{strTime}")
  elif 'open code' in query:
      codePath = "C:\\Users\\ayyap\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(codePath)
  elif 'email to harry' in query:
      try:
          speak("What should I say?")
          content= takeCommand()
          