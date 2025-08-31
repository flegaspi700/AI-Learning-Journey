# -----------------------------------------------------------------------------------------
# Voice-Controlled Assistant
#
# To run this script, you need to install the following libraries:
# pip install -r requirements.txt
#
# You might also need to install PyAudio separately if you encounter issues.
# For Windows, you can often use: pip install pipwin; pipwin install pyaudio
# For Mac: brew install portaudio; pip install pyaudio
# For Linux: sudo apt-get install python3-pyaudio
# -----------------------------------------------------------------------------------------

import speech_recognition as sr
import pyttsx3
import os
import datetime
import webbrowser

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    """Listens for a command from the user and transcribes it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-us').lower()
        print(f"You said: {command}\n")
    except Exception as e:
        print(e)
        # speak("I didn't catch that. Please try again.")
        return "None"
    return command

def main():
    """Main function to run the voice assistant."""
    speak("Voice assistant activated. Say 'computer' to give a command.")

    while True:
        print("Listening for wake word...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                wake_word = recognizer.recognize_google(audio, language='en-us').lower()
                print(f"Heard: {wake_word}")

                if "computer" in wake_word:
                    speak("Yes?")
                    command = listen_for_command()

                    if 'hello' in command:
                        speak("Hello! How are you?")

                    elif 'what time is it' in command:
                        now = datetime.datetime.now().strftime("%I:%M %p")
                        speak(f"The current time is {now}.")

                    elif 'open calculator' in command:
                        speak("Opening calculator.")
                        os.system('calc') # For Windows

                    elif 'search for' in command:
                        search_query = command.replace("search for", "").strip()
                        if search_query:
                            url = f"https://www.google.com/search?q={search_query}"
                            webbrowser.open(url)
                            speak(f"Here are the search results for {search_query}.")
                        else:
                            speak("What would you like me to search for?")
                    
                    elif 'exit' in command or 'quit' in command:
                        speak("Goodbye!")
                        break
                    
                    elif command != 'None':
                        speak("Sorry, I don't understand that command yet.")

            except sr.WaitTimeoutError:
                # This is expected when there's silence, just continue listening
                pass
            except sr.UnknownValueError:
                # This is expected when speech is not understood
                pass
            except Exception as e:
                print(f"An error occurred: {e}")
                # speak("Sorry, I'm having trouble right now.")

if __name__ == "__main__":
    main()
