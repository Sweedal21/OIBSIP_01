import pyttsx3 as pts
import speech_recognition as sr
import datetime as dt
import webbrowser as wb
import os 
import wikipedia as wk
import gtts  
from playsound import playsound  

voice_engine = pts.init('sapi5')
voices = voice_engine .getProperty('voices')
voice_engine .setProperty('voices',voices[0].id)
def sound_output(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()
def greet():
    time=int(dt.datetime.now().hour)
    if time>=0 and time<12:
        sound_output('Good morning!')
    elif time>=12 and time<16:
        sound_output('Good Afternoon!')
    elif time>=16 and time<21:
        sound_output('Good Evening')    
    else:
        sound_output('Good Night')
    sound_output("How may i help you?")
def current_time():
    now_time= dt.datetime.now()
    hour=now_time.strftime("%I")
    mins=now_time.strftime("%M")
    am_pm=now_time.strftime("%p")  
    sound_output(f'The time is {hour}:{mins} {am_pm}.')
def current_date():
    now_date= dt.datetime.now()
    year=now_date.strftime("%Y")
    month=now_date.strftime("%m") 
    day=now_date.strftime("%d") 
    sound_output(f'The date is {day}:{month}:{year}.')
def user_command_input():
    mic =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening the command ")
        mic.pause_threshold = 1
        audio = mic.listen(source)
    try:
        print('recognizing the command')
        user_command = mic.recognize_google(audio, language='en-in')
        print(f"user input: {user_command}\n")
    except Exception as e:
        print("Please repeat it again")
        sound_output("Sorry, I could not understand. Could you please repeat that again?")
        return "none"
    return user_command

if __name__== "__main__":
    greet()
    while True:
        user_command = user_command_input().lower()
        if 'hello' in user_command:
            sound_output('Hello Dear, How i can answer you?')
        elif 'open youtube' in user_command:
            wb.open("youtube.com")
        elif 'open google' in user_command:
            wb.open("google.com")
        elif 'time' in user_command:
            current_time()
        elif 'date' in user_command:
            current_date()
        elif "exit" or "bye" in user_command:
            sound_output("Goodbye! Have a great day.")
            quit()






