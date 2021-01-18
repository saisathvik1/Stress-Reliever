import pyttsx3

ask = pyttsx3.init()
ask.say("Hello Sathvik, this is Jarvis! How are you feeling now??")
ask.runAndWait()
data = input("Enter here: ")
# Initializing assistant
assistant = pyttsx3.init()

if "stress" in data:
    assistant.say("Chill dude! Leave your PC and take some break!")
    assistant.runAndWait()

elif "good" in data:
    if "not" in data:
        assistant.say("Don't worry sathvik! Work hard and expect good results!")
        assistant.runAndWait()
    else:
        assistant.say("Hurray! ")

elif "depress" in data:
    assistant.say("Don't take dangerous decisions, talk to your loved ones and fix your problem")
    assistant.runAndWait()

elif "success" in data:
    if "unsuccess" or "not" in data:
        assistant.say("Don't worry Sathvik, Failure is the first step towards success!")
        assistant.runAndWait()
    else:
        assistant.say("I'm proud of you sathvik! Let your loved ones also know your achievement")
        assistant.runAndWait()

elif "happy" in data:
    if "not happy" in data:
        assistant.say("Don't worry sathvik!")
        assistant.runAndWait()
    elif "unhappy" in data:
        assistant.say("Don't worry sathvik!")
        assistant.runAndWait()
    else:
        assistant.say("Party hard bro!")
        assistant.runAndWait()

elif "great" in data:
    assistant.say("I'm proud of you sathvik!")
    assistant.runAndWait()

elif "love you" in data:
    assistant.say("It's pleasure helping you sathvik!")
    assistant.runAndWait()

elif "bored" in data:
    assistant.say("Relax dude! Take some break and start your work again!")
    assistant.runAndWait()

else:
    assistant.say("I'm not familiar with your feeling! sorry!")
    assistant.runAndWait()
