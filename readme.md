# 🧠 JarvisAI – Your Personal AI Voice Assistant

![JarvisAI Banner](https://i.imgur.com/ZfqjVuG.png)

JarvisAI is a Python-powered, voice-activated virtual assistant that responds to your commands just like Iron Man’s Jarvis. With features like AI-powered chatting (using OpenAI), speech recognition, camera control, and more — this assistant makes your desktop intelligent and interactive!

---

## 🔥 Features

- 🎙️ **Speech Recognition** – Talk to your assistant naturally.
- 🗣️ **Text-to-Speech** – Realistic voice replies using `pyttsx3`.
- 🤖 **GPT-4o-mini Integration** – Chat with AI via OpenAI API.
- 🌐 **Smart Web Commands** – Open YouTube, Google, GitHub & more.
- 📷 **Camera Control** – Use voice to open/close your webcam.
- 🕒 **Time Updates** – Ask for the current time.
- ⚙️ **App Launcher** – Launch tools like Postman by voice.
- 💾 **AI Response Logging** – Logs AI replies in local text files.

---

## 📸 Demo

https://github.com/yourusername/JarvisAI/assets/demo.mp4 *(Insert your screen recording link here)*

---

## 🧱 Built With

| Technology       | Purpose                  |
|------------------|---------------------------|
| `Python 3`       | Main programming language |
| `OpenAI API`     | AI-based chat responses   |
| `SpeechRecognition` | Voice input             |
| `Pyttsx3`        | Text-to-speech engine     |
| `OpenCV`         | Camera control            |
| `Threading`      | Async camera management   |

---

## 📁 Project Structure

```plaintext
JarvisAI/
│
├── OpenAI/               # Saved AI response logs
├── myenv/                # Virtual environment (excluded from repo)
├── config.py             # Contains your OpenAI API key (do NOT upload)
├── main.py               # Main assistant script
└── requirements.txt      # List of dependencies

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/JarvisAI.git
cd JarvisAI

## Install Dependencies

pip insatll -r requirements.txt