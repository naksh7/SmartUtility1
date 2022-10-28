import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import pyautogui



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search for' in command:
        search = command.replace('search for','')
        print('searching for')
        webbrowser.open('https://www.google.com/search?q='+search,new=2)
    elif 'screenshot' in command:
        pyautogui.press('printscreen')
    elif 'partial screenshot' in command:
        pyautogui.press('win','shift','s')
    elif 'login' in command:
        os.startfile("C:\\Users\\aknagpur\\Softwares\\AutoIT\\Scripts\\Login.exe")

    else:
        talk('kai bi vicharate ka be')

