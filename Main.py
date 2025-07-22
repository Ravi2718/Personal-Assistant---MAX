import os
import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui
import webbrowser
import time
import random
import wolframalpha
import subprocess
import sys
import keyboard
from playsound import playsound
from datetime import datetime

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Set voice rate to 160
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice

# Initialize the recognizer for speech recognition
recognizer = sr.Recognizer()

# WolframAlpha client
client = wolframalpha.Client('YOUR_ID')

# Function to speak text
def speak(text):
    print(text)  # Print the response for debugging
    engine.say(text)
    engine.runAndWait()

# Function to play the activation sound
def play_activation_sound():
    playsound("Voicy_Siri sound effect.mp3")

# Function to play the end sound
def play_end_sound():
    playsound("end_sound.mp3")

# Listen for a wake word ("MAX")
def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening for 'MAX'...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            if "max" in command:
                print("Wake word 'MAX' detected!")
                play_activation_sound()  # Play activation sound
                return True
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"Error: {e}")
    return False

# Listen for commands after detecting the wake word
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")
            return command
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"Error: {e}")
    return None

# Execute commands based on user input
def execute_command(command):
    command = command.lower()
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")
    elif "take screenshot" in command:
        speak("Taking screenshot")
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.expanduser('~') + "/Pictures/screenshot.png")
        speak("Screenshot saved in your pictures folder.")
    elif "convert to text" in command:
        speak("Please speak your text now.")
        text = listen_for_command()
        if text:
            speak(f"Your text is: {text}")
            # Optionally you can output the text to Word or Notepad
            # Using `pyautogui` to simulate typing in an open text editor
            pyautogui.typewrite(text)
    elif "what is the date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")
    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "tell me a joke" in command:
        try:
            res = client.query("joke")
            joke = next(res.results).text
            speak(f"Here's a joke: {joke}")
        except Exception as e:
            speak("Sorry, I couldn't fetch a joke.")
    elif "tell me about" in command:
        query = command.replace("tell me about", "").strip()
        speak(f"Here is some information about {query}")
        try:
            res = client.query(query)
            info = next(res.results).text
            speak(info)
        except Exception as e:
            speak(f"Sorry, I couldn't find information about {query}")
    elif "lock screen" in command:
        speak("Locking the screen now.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "play music" in command:
        speak("Playing music on YouTube")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Example random video link
    elif "minimize all windows" in command:
        keyboard.press_and_release('win + d')
        speak("All windows minimized.")
    elif "open chrome and search" in command:
        search_query = command.replace("open chrome and search", "").strip()
        speak(f"Searching for {search_query} on Chrome.")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "minimize all windows" in command:
        keyboard.press_and_release('win + d')
        speak("All windows minimized.")
    else:
        speak("Sorry, I didn't understand that.")

# Main assistant loop
def assistant_loop():
    while True:
        if listen_for_wake_word():  # Wait for the wake word "MAX"
            time.sleep(0.5)  # Delay after detecting the wake word
            command = listen_for_command()  # Listen for the command immediately after detecting "MAX"
            if command:
                execute_command(command)
                play_end_sound()  # Play the end sound after the command is executed
            else:
                print("No command detected.")
                play_end_sound()  # Play the end sound if no command is detected

# Start the assistant
if __name__ == "__main__":
    try:
        print("Calibrating microphone for ambient noise...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
        print("Microphone calibration complete.")
        assistant_loop()
    except KeyboardInterrupt:
        print("\nAssistant terminated.")
