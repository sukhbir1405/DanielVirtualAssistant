import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")  
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def Hello():
      
    # This function is for when the assistant 
    # is called it will say hello and then 
    # take query
    speak("hello sir I am your desktop assistant Daniel Tell me how may I help you")
  
  
def Take_query():
  
    # calling the Hello function for 
    # making it more interactive
    Hello()
      
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
    while(True):
          
        # taking the query and making it into
        # lower case so that most of the times 
        # query matches and we get the perfect 
        # output
        query = takeCommand().lower()
        if "open my github page" in query:
            speak("Opening your page ")
              
            # in the open method we just to give the link
            # of the website and it automatically open 
            # it in your default browser
            webbrowser.open("https://github.com/sukhbir1405")
            continue
          
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        
        elif "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue
        
              
        elif "which day it is" in query:
            tellDay()
            continue
          
        elif "tell me the time" in query:
            tellTime()
            continue
          
        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exicting things")
            exit()
          
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6)) 

        elif 'play music' in query:
            music_dir = 'D:\\audio songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 

        elif "how are you" in query:
            speak("I'm fine, glad you asked me that")

        elif "daniel" in query:
             
            wishMe()
            speak("Daniel 1 point o in your service Mister")
            speak('Singh')  

        elif 'email to kamal ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sukhbirbhullar8384@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Sukhbir bhai. I am not able to send this email")  

        elif "from wikipedia" in query:
              
            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
              
            # it will give the summary of 4 lines from 
            # wikipedia we can increase and decrease 
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
          
        elif "tell me your name" in query:
            speak("I am Daniel. Your deskstop Assistant") 
  
if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Take_query()