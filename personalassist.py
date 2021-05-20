import speech_recognition as sr
import pyttsx3 as tts
from datetime import datetime
import wikipedia as wiki
import webbrowser as web
from ecapture import ecapture as ec
import wolframalpha as w
import time
jarvis=tts.init()
jarvis.setProperty('rate',180)
def listen():
  try:
    recon = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        recon.adjust_for_ambient_noise(source)
        audio=recon.listen(source,timeout=5,phrase_time_limit=10)
    text=recon.recognize_google(audio)
    print(" User said : ",text)
    return str(text.lower())
  except:
      jarvis.say("I can't understand you")
      jarvis.runAndWait()
      return None
def greet():
    x=datetime.now().hour
    if(x>=0 and x<=12):
        jarvis.say("Good Morning!")
        jarvis.runAndWait()
    elif(x>=12 and x<=15):
        jarvis.say("Good Afternoon!")
        jarvis.runAndWait()
    elif(x>=15 and x<=19):
        jarvis.say("Good Evening!")
        jarvis.runAndWait()
    else:
        jarvis.say("Hello")
        jarvis.runAndWait()
if __name__=='__main__':
    greet()
    jarvis.say("I'm JARVIS, how can I help you?")
    jarvis.runAndWait()
    while(True):
        text = listen()
        if text==None:
            continue
        elif "what" in text and "time" in text or"current time" in text:
           jarvis.say("time is "+str(x.datetime.now()))
           jarvis.runAndWait()
        elif "what" in text and "day" in text:
           jarvis.say("today is "+str(datetime.now().day))
           jarvis.runAndWait()
        elif "what" in text and "month" in text:
           x="this is "+str(datetime.now().month)
           jarvis.say(x)
           jarvis.runAndWait()
        elif "open" in text and "youtube" in text:
           jarvis.say("opening youtube in browser")
           jarvis.runAndWait()
           web.open_new_tab("www.youtube.com")
        elif "open" in text and "facebook" in text:
           jarvis.say("opening facebook in browser")
           jarvis.runAndWait()
           web.open_new_tab("www.facebook.com")
        elif "open" in text and "twitter" in text:
           jarvis.say("opening twitter in browser")
           jarvis.runAndWait()
           web.open_new_tab("www.twitter.com")
        elif "open" in text and "reddit" in text:
           jarvis.say("opening reddit in browser")
           jarvis.runAndWait()
           web.open_new_tab("www.reddit.com")
        elif "who are you?" in text:
           jarvis.say("I'd like to keep that secret to myself, unlike humans i care about my privacy")
           jarvis.runAndWait()
        elif "search" in text:
           jarvis.say("Here you go, use google search")
           jarvis.runAndWait()
           web.open_new_tab("www.google.com")
        elif "how" in text or "weather" in text or "why" in text:
           client=w.Client('VH6GPR-GY7TT3X399')
           res=client.query(text)
           res=next(res.results).text
           jarvis.say(res)
           jarvis.runAndWait()
        elif "who" in text or "what" in text or "where" in text:
           jarvis.say("According to wiki ")
           jarvis.runAndWait()
           jarvis.say(wiki.summary(text,2))
        elif "take" in text and "photo" in text:
           jarvis.say("Say cheese")
           jarvis.runAndWait()
           ec.capture(0,True,False)
           jarvis.say("Excellent photo it is")
           jarvis.runAndWait()
        elif "stop" in text or "goodbye" in text or "bye" in text or "exit" in text:
           jarvis.say("Its been nice talking to you")
           jarvis.say("Until next time.")
           jarvis.runAndWait()
           print("jarvis has been shutdown")
           break
        else:
            jarvis.say("According to wikipedia ")
            jarvis.runAndWait()
            jarvis.say(wiki.summary(text, 1))
        jarvis.say("Is there anything i can do")
        jarvis.runAndWait()










