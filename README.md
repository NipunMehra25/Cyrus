# Cyrus AI Assistant 🤖

An intelligent voice-controlled AI assistant built with Python, featuring speech recognition, text-to-speech, screen analysis, code review, and various automation capabilities powered by Google's Gemini AI.

## ✨ Features

### 🎤 Voice Commands
- **Voice Recognition**: Natural speech-to-text conversion
- **Text-to-Speech**: Responsive voice feedback
- **Conversational AI**: Powered by Google Gemini 2.0 Flash model

### 🖥️ Screen Analysis
- **Screenshot Analysis**: Describe what's currently on your screen
- **Screen Content Search**: Find specific items on your screen
- **Visual Understanding**: AI-powered image analysis

### 💻 Code Analysis
- **Multi-language Support**: Automatic programming language detection
- **Error Detection**: Find bugs and syntax errors with line numbers
- **Code Review**: Performance analysis and optimization suggestions
- **Complexity Analysis**: Time and space complexity evaluation

### ⚡ System Automation
- **Window Management**: Minimize tabs, close applications
- **Browser Control**: Open Chrome, search the web
- **Application Launcher**: Quick access to applications
- **WhatsApp Integration**: Direct access with password protection

### ⏰ Productivity Tools
- **Smart Alarms**: Set timers with voice commands
- **Clipboard Integration**: Automatic code and analysis copying
- **Multi-tasking**: Handle multiple commands efficiently

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- Windows OS (for some automation features)
- Microphone for voice input
- Tesseract OCR installed

### Required Dependencies

```bash
pip install pyautogui
pip install speechrecognition
pip install pyttsx3
pip install google-generativeai
pip install pyperclip
pip install pytesseract
pip install pillow
pip install numpy
pip install easyocr
```

### Additional Setup

1. **Install Tesseract OCR**:
   - Download from: https://github.com/tesseract-ocr/tesseract
   - Install to: `C:\Program Files\Tesseract-OCR\`

2. **Get Google Gemini API Keys**:
   - Visit: https://makersuite.google.com/app/apikey
   - Generate API keys and replace in the `api_keys` list

3. **Update File Paths**:
   - Replace image paths in the code with your actual screenshot paths
   - Update Tesseract path if installed elsewhere

## 🚀 Usage

### Starting Cyrus
```bash
python cyrus_assistant.py
```

### Voice Commands

#### General Conversation
- "Hello" / "Hi" / "How are you?"
- "What is your name?"
- "What do you do?"

#### Screen Analysis
- "What's on my screen?"
- "Describe my screen"
- "Analyze my screen"

#### Code Analysis
- "Analyze my code"
- "Check code"
- "Find errors"
- "Review code"

#### System Control
- "Minimize" / "Minimize all tabs"
- "Close"
- "Open Google" / "Open Chrome"
- "Open WhatsApp"

#### Productivity
- "Set an alarm for 5 minutes"
- "Set alarm for 30 seconds"

#### Search
- "Find [item] on screen"
- "Search for [query]"

#### Exit
- "Exit" / "Stop" / "Quit"

## 🔧 Configuration

### API Key Setup
Replace the placeholder API keys in the code:
```python
api_keys = [
    "YOUR_GEMINI_API_KEY_1",
    "YOUR_GEMINI_API_KEY_2",
    # Add more keys for better reliability
]
```

### Voice Settings
Adjust speech rate and voice properties:
```python
engine.setProperty("rate", 180)  # Speech speed
```

### Screen Region
Configure screen capture area:
```python
x, y, width, height = 122, 171, 1625, 713  # Adjust as needed
```

## 📁 Project Structure

```
cyrus/
│
├── main.py                # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── img/                   # Screenshot images for UI automation
│   ├── image.png
│   ├── Screenshot1.png
│   └── Screenshot2.png
└── docs/                  # Additional documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security Notes

- Store API keys securely (consider using environment variables)
- Be cautious with screen analysis in sensitive environments
- WhatsApp integration requires password input for security

## 🐛 Troubleshooting

### Common Issues

**"API key issue detected"**
- Verify your Gemini API keys are valid
- Check if you've exceeded API quotas

**"No text found" during code analysis**
- Ensure your code editor is focused
- Try selecting code manually before running analysis

**Voice recognition not working**
- Check microphone permissions
- Ensure microphone is not muted
- Try adjusting microphone sensitivity

**Screen automation failing**
- Update screenshot paths in the code
- Adjust confidence levels for image recognition
- Ensure target applications are visible

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for conversational capabilities
- Python community for excellent libraries
- Contributors and testers

## 📧 Contact

For questions, suggestions, or support:
- Create an issue on GitHub
- Fork and contribute to the project

---

**Note**: This assistant is designed for educational and productivity purposes. Always ensure you comply with the terms of service of the APIs and services used.
