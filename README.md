# Installation Guide

Before running the Virtual Assistant project, install Python (version 3.8 or above) on your system.

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
cd <repository-folder-name>
```

## Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

## Step 3: Install Required Python Modules

Open Command Prompt (CMD) or Terminal and run the following commands:

```bash
pip install gtts
pip install SpeechRecognition
pip install playsound==1.2.2
pip install PyAudio
```

Alternatively, create a `requirements.txt` file with the following content:

```txt
gtts
SpeechRecognition
playsound==1.2.2
PyAudio
```

Then install all dependencies using:

```bash
pip install -r requirements.txt
```

## Note for PyAudio Installation

If you encounter an error while installing `PyAudio`, use one of the following commands:

```bash
pip install pipwin
pipwin install pyaudio
```

or

```bash
python -m pip install PyAudio
```

## Run the Project

After installing all required modules, run the project using:

```bash
python virtual_assistant.py
```

## Required Libraries

* gTTS (Google Text-to-Speech)
* SpeechRecognition
* playsound
* PyAudio
* smtplib (Built-in Python module)
* webbrowser (Built-in Python module)
* os (Built-in Python module)
* uuid (Built-in Python module)
* time (Built-in Python module)
