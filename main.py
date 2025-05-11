import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import cv2
import threading
import os
import random

import openai
from openai import OpenAI
from config import apikey
openai.api_key = apikey

# Global variables for camera
cap = None
camera_open = False

chatStr = ""

def chat(prompt):
    global chatStr
    
    client = OpenAI(api_key=apikey)
    chatStr += f"Deep: {prompt}\nJarvis: "
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content": f"{chatStr}"}]
    )

    try:
        say(response.choices[0].message.content)
        chatStr += f"{response.choices[0].message.content} + \n"
        
        # with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as file:
        #     file.write(text)
        
    except Exception as e:
        print("Error:", e)


def ai(prompt):
    client = OpenAI(api_key=apikey)
    text = f"OpenAI response for prompt: {prompt} \n *********************************\n\n"
    
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": f"{prompt}"}
    ]
    )

    try:
        text += response.choices[0].message.content + "\n"
        if not os.path.exists("OpenAI"):
            os.makedirs("OpenAI")
        
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as file:
            file.write(text)
        
    except Exception as e:
        print("Error:", e)
        
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            print("Sorry, I did not understand that.")
            return ""

def open_camera():
    global cap, camera_open
    if camera_open:
        say("Camera is already open.")
        return

    say("Opening camera")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        say("Cannot open camera")
        return

    camera_open = True
    while camera_open:
        ret, frame = cap.read()
        if not ret:
            say("Failed to grab frame")
            break
        cv2.imshow('Camera', frame)

        # Check every 1ms for a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera_open = False
            break

    # Properly close everything inside the thread
    cap.release()
    cv2.destroyAllWindows()
    say("Camera closed")

def close_camera():
    global camera_open
    if camera_open:
        say("Closing camera")
        camera_open = False  # Let the thread exit and clean up
    else:
        say("Camera is not open")

if __name__ == "__main__":
    print("This is the main module.")
    say("Hello, I am your assistant.")

    while True:
        query = takeCommand()

        # Site launching
        sites = [
            ["youtube", "https://www.youtube.com/"], 
            ["google", "https://www.google.com/"], 
            ["facebook", "https://www.facebook.com/"], 
            ["instagram", "https://www.instagram.com/"], 
            ["twitter", "https://twitter.com/"], 
            ["linkedin", "https://www.linkedin.com/"], 
            ["reddit", "https://www.reddit.com/"], 
            ["docker", "https://docs.docker.com"],
            ["github", "https://www.github.com/"],
            ["wikipedia", "https://www.wikipedia.org/"]
        ]
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        # Time
        if "the time".lower() in query.lower():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strftime}")
            say(f"Sir, the time is {strftime}")

        # Open Camera (run in thread)
        elif "open the camera".lower() in query.lower():
            threading.Thread(target=open_camera, daemon=True).start()

        # Close Camera
        elif "close the camera".lower() in query.lower():
            close_camera()
            
        elif "open postman".lower() in query.lower():
            say("Opening Postman")
            os.startfile("C:\\Users\\Deep\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Postman\\Postman.lnk")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
            
        elif "Jarvis Quit".lower() in query.lower():
            say("Goodbye! Call me if you need anything.")
            break
        
        elif "reset chat".lower() in query.lower():
            chatStr = ""
            say("Chat reset")
        
        elif "chat".lower() in query.lower():
            say("Chatting with you")
            print("Chatting..")
            chat(query)