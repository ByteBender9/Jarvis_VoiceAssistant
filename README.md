# 🎙️ Jarvis - Desktop Voice Assistant

A Python-based desktop voice assistant that automates everyday desktop tasks using voice commands.

---

## 👨‍💻 Developed By

**Kushal Sarkar**

🎓 Diploma in Computer Science & Engineering

🏫 Techno Polytechnic Durgapur

GitHub: https://github.com/ByteBender9

Repository: https://github.com/ByteBender9/Jarvis_VoiceAssistent

---

## 📌 Introduction

Jarvis is a Python-based desktop voice assistant that enables users to interact with their computer using voice commands. It leverages speech recognition and text-to-speech technologies to automate everyday tasks such as searching the web, opening websites, playing music, taking notes, capturing screenshots, and retrieving information from Wikipedia.

The assistant greets the user based on the current time, listens to voice commands through the microphone, processes them, and performs the requested actions, providing a hands-free and user-friendly computing experience.

---

## 📌 Features

* 🎤 Voice-controlled interaction
* 👋 Greets users based on the current time
* 🕒 Displays current date and time
* 🌐 Opens websites
* 🔍 Google search
* 📖 Wikipedia search
* 🎵 Plays music
* 📝 Creates and saves notes
* 📷 Takes screenshots with custom filenames
* 🔒 Face authentication support
* 💻 Desktop automation
* 📴 Voice command to exit the assistant

---

## 🛠️ Tech Stack

- Python
- HTML
- CSS
- JavaScript
- SQLite

---

## 📌 Python Libraries

🔹 pyttsx3

Offline text-to-speech engine used to convert text into natural speech.

🔹 SpeechRecognition

Captures voice commands through the microphone and converts speech into text.

🔹 Datetime

Provides the current date and time and generates time-based greetings.

🔹 Wikipedia

Fetches summaries and information from Wikipedia.

🔹 Webbrowser

Opens websites directly in the user’s default browser.

🔹 OS

Performs operating system tasks such as launching applications and managing files.

🔹 Random

Generates random values for assistant responses where required.

🔹 PyAutoGUI

Automates keyboard and mouse actions, including taking screenshots.

---

## 📂 Project Structure

```
Jarvis_VoiceAssistent/
│
├── engine/
│   ├── auth/
│   ├── command.py
│   ├── config.py
│   ├── helper.py
│   └── ...
│
├── www/
│   ├── assets/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── main.py
├── run.py
├── device.sh
├── README.md
├── LICENSE
└── requirements.txt
```
---

## 📋 Requirements

- Python 3.9+
- Microphone
- Internet connection (for online features)
- Webcam (for face authentication)

---


## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/ByteBender9/Jarvis_VoiceAssistent.git
```

### Navigate to the project

```bash
cd Jarvis_VoiceAssistent
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the voice assistant by running:

```bash
python run.py
```

or

```bash
python main.py
```

(**Note:** Run `main.py` or `run.py` depending on your project configuration.)

---

## 📌 Why Use Jarvis?

* Hands-free computer interaction
* Improves productivity by automating routine tasks
* Easy to install and use
* Beginner-friendly interface
* Supports both voice and keyboard input
* Can be customized with additional commands

---

## 📌 Advantages

* User-friendly interface
* Hands-free desktop control
* Easily customizable
* Offline text-to-speech support
* Helpful for accessibility
* Modular and expandable architecture

---

## 📌 Limitations

* Voice recognition accuracy decreases in noisy environments
* Limited natural language understanding compared to cloud AI assistants
* Performance depends on microphone quality
* Requires Python dependencies to be installed

---

## 📌 Future Enhancements

* AI chatbot integration (GPT/LLMs)
* Smarter Natural Language Processing
* Home automation support
* Cross-platform compatibility
* Mobile application integration
* Personalized user profiles
* Email and calendar management
* Advanced desktop automation

---

## 📌 Conclusion

Jarvis demonstrates how artificial intelligence and speech recognition can simplify everyday computer interaction through voice commands. The project combines multiple Python libraries to provide a practical desktop automation solution and serves as a strong foundation for building more advanced AI-powered personal assistants in the future.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📬 Contact
**Kushal Sarkar**
- GitHub: https://github.com/ByteBender9
- LinkedIn: https://www.linkedin.com/in/kushalsarkar
- Email: connect.kushals@gmail.com