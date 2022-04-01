#This package is for HariniAlexa to listen to the speech being spoken
import speech_recognition as sr
#This package is for HariniAlexa to speak back after listening to the audio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#listener is a variable to call the package functions under speech_recognition through the variable we assigned to import it (sr)
#sr.Recogniser() creates an instance so that listener can be actively called through the instance as an object
listener = sr.Recognizer()
#pyttsx3 is initialised through init()
engine = pyttsx3.init()
#To change and choose the tones and voices that this alexa can provide, we can do the following
#The getProperty below will get all the voices that you are setting into the variable
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
#Alexa will now say the following
#engine.say('Hi My name is Harini. What can I do for you today')
#Then after saying the above, the program will wait for other functions to be completed through the runandWait function
#Let us nowmake this dynamic by doing th following
def talk(text):
    engine.say(text)
    engine.runAndWait()
#In the above, text is now a parameter so whenever the function is called, text variable will be spoken
#REFPT1:So now, instead of printing command, we can change it to talk that will call the function
def take_command():
    try:
        #source is the source of our audio
        #Using your Microphone as a source and then calling the speech recogniser to listen to the source. And once the source is taken, can manipulate easily
        with sr.Microphone() as source:
            #To let the user know that alexa is listening to them speak now, we can write the following
            print('listening...')
            #voice is a variable which will store what the listener variable (from listener = sr.Recogniser()) listens from source
            voice = listener.listen(source)
            #We now have the source as voice. We can convert voice to text
            #Here in a variable command that calls google api through listener.recognise_google and the audio is passed to google
            #Now, google will return the text from the voice and to make sure it is working we print as shown below
            command = listener.recognize_google(voice)
            #Converts command to lowercase
            command = command.lower()
            #if alexa is heard from the voice, then the command is printed
            if 'alexa' in command:
                #To make sure alexa is not repeated when she talks back
                command = command.replace('alexa', '')
                #REFPT1(Please refer to explanation in REFPT1)
                print('Hi Harini')

    except:
        pass
    return command

def run_alexa():
    #This function calls the above take_command function
    command = take_command()
    print(command)
    #Processing the command over here
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        #Plays the song on youtube using the playwhatkit package's function
        pywhatkit.playonyt(song)
    elif 'time' in command:
        #To get 24hr format we can do %H%M%S
        #To get 12hr format with AM or PM for time we do the following
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        #Gets 1 line of information about the person specified
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'type what I say' in command:
        print(command)
        talk('Typing what you said')
    else:
        talk('Done! Speak again')
        run_alexa()

run_alexa()
