from platform import uname
from random import choice
from urllib.parse import quote
import pyttsx3 #text to speech
import pyaudio  # to talk back
import speech_recognition as sr    #to take commend from speech
import datetime   # date time 
from tkinter import * #fot gui app
import wikipedia   #browse wikipedia
import webbrowser   #browse websites
import pywhatkit   # play song direct form youtube
import pyjokes  #for jokes
import os # to give the os permission
import random # for random choice 
import sys #to acess system files
import operator #for using operator voice 
import cv2 #import camera functions of os






engine = pyttsx3.init('sapi5') # taking sapi5 as speech application program
voices = engine.getProperty('voices') #taking the of voices
engine.setProperty('voice',voices[0].id) #gender of voice
engine.setProperty('rate',178) # rate of t speaking per min



def speak(audio): # to speak with the help of the speaker
    engine.say(audio)  # to speak
    engine.runAndWait() # wait after speaking
    
def greetings():   # greeting the uesr 
    hour = int(datetime.datetime.now().hour) # date time function 
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak("I am Oxy. Please tell me how may I assist you")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        speak("I am Oxy. Please tell me how may I assist you")
    else:
        speak("Good   Evening!")
        speak("I am Oxy. Please tell me how may I assist you")

def takeCommand():
    
    r = sr.Recognizer() #recognise the voice 
    with sr.Microphone() as source: # taking permission of microphone
        print('Listening...')
        r.pause_threshold = 1  # for loudness of voice
        r.adjust_for_ambient_noise(source) # for noise reduction
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition. and turn it into string
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)
        speak ("Say that again please....")  
        print("Say that again please....")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def usrname():
    speak('what should i call you sir')
    uname=takeCommand()
    speak('ok sir.your name is')
    speak(uname)

#for calculator

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = iCalc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q))

        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')


            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))

    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
                #for calculator

if __name__ == "__main__":  #main function
     greetings ()
     

     while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '') #replace the wikipedia frm the command and search the rst in wikipedia
            results = wikipedia.summary(query, sentences=2)  # take the paragraph frm wikipedia and read 3 sentences
            speak("According to Wikipedia")  #will ad this in front of the text
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            #webbrowser.open("youtube.com") #browse youtube
            url = "youtube.com"
            chrome_path ='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")  #browse google

        elif 'are you single' in query:
            speak("its complecated.Currently wifi wants a relation with me.")

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%I:%M: %p") #printing  current date time
            print(Time)    
            speak(f"Sir, the time is {Time}") 

        elif 'play' in query:
            songyt=query.replace('play', '') # cancels the word play and rest of the commend  is saved in querry
            speak('playing...' + songyt)
            pywhatkit.playonyt(songyt) #direct to youtube and play the song
        elif 'joke' in query:
            tjoke=pyjokes.get_joke() # to get random jokes
            print(tjoke)
            speak(tjoke)
        elif 'song'in query:
            music_dir = "E:\\audio (1)" #giving directory
            songs= os.listdir(music_dir)  #song played frm directory
            rd = random.choice(songs)   
            os.startfile(os.path.join(music_dir, rd))  # play song
        elif 'what are you doing' in query:
            speak('nothing.Just laughing at my own jokes')
        elif 'your name' in query:
            speak('i am oxy, an artificial intelligance created by rajesh')
        elif 'my name' in query:
            speak('your name is Rajesh Roy. and your birth say is 3rd june 2000')       
        elif 'take a picture' in query:
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("NewPicture.jpg",frame)
                result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
 
        elif 'open camera' in query:
            videoCaptureObject = cv2.VideoCapture(0)
            while(True):
                 ret,frame = videoCaptureObject.read()
                 cv2.imshow('Capturing Video',frame)
                 if(cv2.waitKey(1) & 0xFF == ord('q')):
                    videoCaptureObject.release()
                    cv2.destroyAllWindows()

        elif 'calculator' in query:
            app().mainloop()


        elif 'stop' in query:
                speak('thanks for using me . have a good day')
                sys.exit()

        elif 'calculate'in query:
            try:
                print(query)
                query = query.replace("calculate", '')
                def get_operator_fn(op):
                    return {
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                '/' : operator.__truediv__,
                'divided by' :operator.__truediv__,
                'divide' :operator.__truediv__,
                'divided' :operator.__truediv__,
                'divide by' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                    }[op]
                def eval_binary_expr(op1,oper,op2):
                    op1=int(op1)
                    op2=int(op2)
                    return get_operator_fn(oper)(op1,op2)
                print(eval_binary_expr(*(query.split())))
                speak(eval_binary_expr(*(query.split())))
            except:
                print('error')
                speak('error')
        elif 'thank u' in query:
            speak("Its my pleasuure to help you")
