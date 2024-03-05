# Voice_Assistant_Jarvis_ChatGPT_API
A Voice Assistant - Jarvis, using Python and based on ChatGPT API to response question.

![Jarvis](https://upload.wikimedia.org/wikipedia/en/e/e0/J.A.R.V.I.S._%28MCU%29.png)

## Getting Started
In order to start this project, you need to run the following code in your command to install the package:
```
pip install openai
```
```
pip install pyttsx3
```
```
pip install speech_recognition
```
Above code will install the `openai`, `pyttsx3` and `speech_recognition` packages and all of its dependencies.

If the `speech_recognition` package didn't install successfully, alternatively you can install the package directly from the source code by cloning the Git repository and running the setup.py script:
```
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
python setup.py install
```

## How to Modify the code:
Before you run the program, you can modify a few line of code.

### 1. Add your ChatGPT API to the code:
Add your ChatGPT API key here `"YOUR_API_KEY"`
```
openai.api_key = "YOUR_API_KEY"
```

### 2. Optional code:
You can choose the voice to male or female by change following setting:
```
engine.setProperty('voice', voice[0].id)
```

```

## How to run the Jarvis:
Run `python Jarvis.py`
```
python Jarvis.py
```

## How to stop the Jarvis:
Say `thank you for your help` to stop the program, if you want to change to other sentence to stop the program, you can modify the following code:
```
if prompt == "thank you for your help":
      # Exit the program
      sys.exit()
```

## Authors
 **Shaun Lin**
 