import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            print(command)

    except:
        pass

    return command


def run():
    try:
        command = take_command()
        if 'play' in command:
            song = command.replace('play','')
            talk("playing "+ song)
            pywhatkit.playonyt(song)
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('current time is ' + time)

        elif 'tell me about' in command:
            person = command.replace('tell me about','')
            info = wikipedia.summary(person,1)
            print("info : " + info)
            talk(info)

        elif 'who is' in command:
            person = command.replace('who is','')
            info = wikipedia.summary(person,1)
            print("info : " + info)
            talk(info)

        elif 'joke' in command:
            talk("here's a joke for you")
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        
        elif 'bored' in command:
            talk("here's a joke for you")
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        else:
            talk('Sorry, say it again')
            
    except:
        talk('Sorry, say it again')


run()