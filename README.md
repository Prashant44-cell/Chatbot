# ChatBot

## Introduction

Welcome to **ChatBot**, a simple yet powerful command-line AI assistant built using Python and powered by Ollama's Phi-3 language model. This project demonstrates the integration of modern AI capabilities with user-friendly interfaces, making conversational AI accessible through a terminal-based application.

The chatbot is designed to provide helpful, polite, and intelligent responses to user queries, maintaining context across conversations. It's an excellent starting point for learning about AI integration, natural language processing, and building interactive applications.

## Features

- **Conversational AI**: Powered by Meta's Phi-3 model (14 billion parameters) via Ollama
- **Context Awareness**: Maintains conversation history for coherent, context-aware responses
- **User-Friendly Interface**: Colored text output for better readability (green for bot, yellow for user)
- **Text-to-Speech Support**: Optional voice output using pyttsx3 (currently commented out in main script)
- **Lightweight Design**: Minimal dependencies and simple command-line interface
- **Error Handling**: Graceful error management for robust operation
- **Easy Exit**: Multiple exit commands for user convenience

## Setup Requirements

Before running the ChatBot, ensure your system meets the following requirements:

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.6 or higher
- **RAM**: At least 4GB (8GB recommended for optimal performance)
- **Storage**: Sufficient space for Ollama and the Phi-3 model (~4GB)

### Software Dependencies
- **Ollama**: Local AI model runner (must be installed and running)
- **Phi-3 Model**: Downloaded and available in Ollama
- **Python Packages**: ollama, colorama, pyttsx3

### Hardware Considerations
The Phi-3 model requires significant computational resources. While it can run on CPU-only systems, a GPU will provide much faster response times.

## Installation

Follow these steps to set up the ChatBot on your system:

### Step 1: Install Ollama
1. Visit [ollama.ai](https://ollama.ai) and download the installer for your operating system
2. Install Ollama following the provided instructions
3. Open a terminal and pull the Phi-3 model:
   ```bash
   ollama pull phi3
   ```
4. Verify the installation by running:
   ```bash
   ollama list
   ```
   You should see `phi3` in the list of available models.

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/ChatBot.git
cd ChatBot
```

### Step 3: Install Python Dependencies
```bash
pip install ollama colorama pyttsx3
```

### Step 4: Verify Installation
Run a quick test to ensure everything is working:
```bash
python -c "import ollama, colorama, pyttsx3; print('All dependencies installed successfully')"
```

## How It Works

### Architecture Overview
The ChatBot operates through a simple yet effective architecture:

1. **Initialization**: The script initializes colorama for colored output and sets up the system prompt
2. **Conversation Loop**: A continuous while loop handles user input and bot responses
3. **Context Management**: Maintains a messages list with the system prompt and recent conversation history
4. **AI Processing**: Sends user input to Ollama's Phi-3 model for processing
5. **Response Generation**: Receives and displays the AI-generated response
6. **History Tracking**: Appends each exchange to the conversation history for context

### Key Components

#### System Prompt
```python
system_prompt = "You are a helpful, polite, and intelligent assistant. Answer all questions clearly and with context."
```
This defines the AI's personality and behavior guidelines.

#### Context Window
```python
short_context = [messages[0]] + messages[-4:]
```
Limits context to the system prompt plus the last 4 exchanges to prevent token overflow and maintain relevance.

#### Error Handling
The try-except block ensures the application continues running even if Ollama encounters issues.

### Data Flow
1. User inputs text
2. Input is appended to messages list
3. Context is prepared (system prompt + recent history)
4. Context sent to Phi-3 model via Ollama API
5. Response received and displayed
6. Response added to messages list for future context

## Usage

### Basic Operation
1. **Start Ollama**: Ensure Ollama is running in the background
2. **Launch ChatBot**:
   ```bash
   python ChatBot.py
   ```
3. **Interact**: Type your questions or statements and press Enter
4. **Exit**: Type `exit`, `quit`, or `bye` to end the session

### Example Session
```
🤖 How can I assist you?
You: Hello, what's the weather like today?
Chatbot: I'm sorry, but I don't have access to real-time weather data. However, I can help you find weather information or suggest ways to check it!
You: Tell me about Python programming
Chatbot: Python is a high-level, interpreted programming language known for its simplicity and readability...
You: bye
Chatbot: See you Again, Goodbye! 👋
```

### Advanced Usage
- **Long Conversations**: The bot maintains context across multiple exchanges
- **Error Recovery**: If Ollama is unavailable, the bot displays error messages and continues
- **Text-to-Speech**: Uncomment the TTS code in `ChatBot.py` for voice responses

## Advantages

### Technical Advantages
- **Local Processing**: All AI processing happens locally, ensuring privacy and no internet dependency
- **Lightweight**: Minimal system requirements compared to cloud-based AI services
- **Customizable**: Easy to modify prompts, add features, or integrate with other systems
- **Open Source**: Built with open-source tools and libraries

### User Experience Advantages
- **Fast Response Times**: Local processing provides quick responses
- **Privacy-Focused**: Conversations stay on your device
- **Accessible Interface**: Simple command-line interface works on any terminal
- **Context Awareness**: Remembers recent conversation for natural dialogue flow

### Development Advantages
- **Educational Value**: Great for learning AI integration and Python development
- **Extensible**: Easy to add new features like GUI, web interface, or additional AI models
- **Cost-Effective**: No API costs or subscription fees
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Disadvantages

### Technical Limitations
- **Resource Intensive**: Requires significant CPU/GPU resources for AI processing
- **Model Size**: Phi-3 model takes up considerable storage space
- **No Real-Time Data**: Cannot access current events, weather, or live information
- **Limited Multimodal**: Text-only interface (no image or voice input)

### User Experience Limitations
- **Command-Line Only**: No graphical user interface
- **Setup Complexity**: Requires Ollama installation and model download
- **Context Window**: Limited to recent conversation history
- **Error Handling**: May require technical knowledge to troubleshoot issues

## Future Improvements

### Planned Features
- **Graphical User Interface**: Web-based or desktop GUI for better accessibility
- **Voice Input**: Speech-to-text integration for hands-free operation
- **Multiple Models**: Support for different Ollama models
- **Conversation Export**: Save chat history to files
- **Plugin System**: Extensible architecture for custom features

### Technical Enhancements
- **Better Error Handling**: More robust error recovery and user feedback
- **Configuration Files**: External config for easy customization
- **Logging**: Comprehensive logging for debugging and analytics
- **Testing Suite**: Unit tests and integration tests
- **Docker Support**: Containerized deployment option

## Troubleshooting

### Common Issues

#### Ollama Not Found
**Error**: `ModuleNotFoundError: No module named 'ollama'`
**Solution**: Install Ollama and ensure it's running:
```bash
pip install ollama
ollama serve
```

#### Model Not Available
**Error**: Model 'phi3' not found
**Solution**: Pull the model:
```bash
ollama pull phi3
```

#### Slow Responses
**Cause**: Insufficient hardware resources
**Solution**: 
- Close other resource-intensive applications
- Consider using a system with more RAM or a GPU
- Use a smaller model if available

#### Import Errors
**Error**: Issues with colorama or pyttsx3
**Solution**: Reinstall dependencies:
```bash
pip uninstall colorama pyttsx3
pip install colorama pyttsx3
```

### Performance Optimization
- Run Ollama with GPU acceleration if available
- Close unnecessary applications during use
- Consider using SSD storage for faster model loading

## Project Structure

```
ChatBot/
├── ChatBot.py          # Main application script
├── new.py              # TTS test script
├── README.md           # This documentation
└── requirements.txt    # Python dependencies (optional)
```

## Dependencies Explained

- **ollama**: Python client for interacting with Ollama API
- **colorama**: Cross-platform colored terminal text
- **pyttsx3**: Text-to-speech conversion library
- **cgi**: Standard library (currently unused, can be removed)

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes on multiple platforms
- Update documentation for new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Prashant Gupta**
- Developer and maintainer of the ChatBot project
- Passionate about AI, Python, and open-source development

## Acknowledgments

- **Microsoft/Ollama**: For providing the Phi-3 model and Ollama platform
- **Open Source Community**: For the amazing libraries used in this project
- **Meta AI**: For developing the Phi-3 language model

## Support

If you encounter issues or have questions:
1. Check the Troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed information about your problem
4. Include your operating system, Python version, and error messages

---

*Last updated: December 29, 2025*
