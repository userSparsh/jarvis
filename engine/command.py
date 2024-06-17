import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")
    # in here 0 index for the Devid voice and 1 for the female voice which is the second voice in this basically 2 voice
    # given in this package by default...
    engine.setProperty("voice" , voices[0].id)

    #rate = engine.getProperty('rate')   # getting details of current speaking rate
    #print (rate)                        #printing current voice rate

    engine.setProperty('rate', 174)    # setting up new voice rate
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()
    # here use this line of code because our input device is microphone..
    with sr.Microphone() as source:
        print("Listening.....")
        eel.DisplayMessage("Listening.....")
        # add threeshold..
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        # in this we are using microphone as a source and if user not speaking then wait 10 second otherwise if speakinf then 
        # # only take conent of 6 second.. 
        audio = r.listen(source, 10, 6)

    # Here is te code for find the error at listing and if correctly listen then return you command

    try:
        print("Recognizing")
        eel.DisplayMessage("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(1)
        
    except Exception as e:
        return ""
    return query.lower()
        
    '''
     except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    
    except Exception as e:
       # print(f"An error occurred: {e}")
        return ""
    
   # return query.lower()


#text = takecommand()

#speak(text)
'''

@eel.expose  # for accessing by the frontend..
def allCommands():

    try:
        query = takecommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)

        else:
            print("not run")

    except:
        print("error")

    eel.ShowHood()