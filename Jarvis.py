import openai
import pyttsx3
import speech_recognition as sr
import sys
import threading

# ChatGPT API client
openai.api_key = "api key enter here"

engine = pyttsx3.init()

voice = engine.getProperty('voices')

engine.setProperty('voice', voice[0].id)

engine.setProperty('volume', 1.0)

engine.setProperty('rate', 150)

r = sr.Recognizer()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def listen():
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    text = r.recognize_google(audio)
    return text
  except Exception as e:
    print("Error: " + str(e))
    return None

def generate_response(prompt):
  completions = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message

speak("Hello, I am Jarvis. How can I help you today?")

while True:
  prompt = listen()
  if prompt is not None:
    if prompt == "thank you for your help":
      # Exit the program
      sys.exit()
    response = generate_response(prompt)
    speak(response)

    timer = threading.Timer(10.0, engine.stop)
    timer.start()

    response = generate_response(prompt)
    speak(response)

    # Cancel the timer if the response finishes speaking before it expires
    timer.cancel()
  else:
    speak("I'm sorry, I didn't understand that.")
