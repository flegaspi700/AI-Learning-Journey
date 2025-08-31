# Python Voice Assistant

This project is a simple voice-controlled assistant built in Python. It can recognize voice commands to perform basic tasks like telling the time, opening applications, and searching the web.

## Features

- **Voice-to-Text:** Transcribes spoken commands into text.
- **Command Execution:** Executes commands based on the transcribed text.
- **Text-to-Speech:** Provides voice feedback to the user.

## Setup and Installation

1.  **Clone the repository or download the files.**

2.  **Navigate to the project directory:**
    ```bash
    cd 002_Voice_Assistant
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    > **Note:** `PyAudio` can sometimes be tricky to install. If you run into issues, you may need to install it manually. Please see the comments at the top of `voice_assistant.py` for platform-specific advice.

## How to Run

Execute the main script from your terminal:
```bash
python voice_assistant.py
```

The assistant will activate. Say the wake word **"computer"** and then give one of the commands below.

## Current Commands

- **"hello"**: The assistant will greet you.
- **"what time is it"**: The assistant will tell you the current time.
- **"open calculator"**: Launches the Windows calculator.
- **"search for [your query]"**: Opens Google with your search query.
- **"exit" / "quit"**: Terminates the assistant.

## Future Enhancements

- [ ] Add more application-launching commands.
- [ ] Integrate with a weather API.
- [ ] Add the ability to tell jokes or fun facts.
- [ ] Improve error handling and user feedback.
