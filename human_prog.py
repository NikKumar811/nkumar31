import pyttsx3 as pt
import os

pt.speak("Welcome to automatic application opener")
start= True
while start:

    print("Enter your requirements: ", end = "")
    pt.speak("Please enter your requirements")
    option = input().lower()

    if "don't" in option or "didn't" in option or "do not" in option:
        print("Ok!! We are not opening app!!")
        pt.speak("Ok!! We are not opening app!!")
   
    elif  ("run" in option or "start" in option or "execute" in option or "open" in option) and ("notepad" in option or "editor" in option) and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening notepad please wait.")
        os.system("start notepad")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and ("chrome" in option or "browser" in option) and ("don't" not in option or "do not" not in option or "didn't" not in option):
        while True:
            print("Enter website name: ", end = "")
            pt.speak("Please enter website name")
            website = input().lower()
            if website.endswith(".com") or website.endswith(".in") or website.endswith(".org"):
                pt.speak("We are opening your website please wait.")
                os.system("start chrome"+" "+ website)
                break
            else:
                print("Enter valid website name")
                pt.speak("Please enter valid website name")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and ("media" in option or "player" in option) and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening windows media player please wait.")
        os.system("start wmplayer")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "calculator" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening calculator please wait.")
        os.system("calc")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "pdf" in option or "pdf viewer" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening PDF Viewer please wait.")
        os.system("start acrord32")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "word" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening MS Word please wait.")
        os.system("start winword")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "excel" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening Excel please wait.")
        os.system("start excel")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "powerpoint" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening powerpoint please wait.")
        os.system("start powerpnt")
    elif ("run" in option or "start" in option or "execute" in option or "open" in option) and "music" in option or "music player" in option and ("don't" not in option or "do not" not in option or "didn't" not in option):
        pt.speak("We are opening music player please wait.")
        os.system("start winamp")
    elif option == "exit" or option  == "close" or "quit" in option:
        pt.speak("Thank you for using application!! Have a nice day!!")
        start = False
    else:
        print("Sorry!! We don't support this")
        pt.speak("Sorry!! We don't support this")
