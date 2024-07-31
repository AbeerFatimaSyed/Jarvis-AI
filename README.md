# JARVIS AI

This project is inspired by the fictional AI assistant J.A.R.V.I.S. from the Iron Man series. It's a voice-activated assistant that can perform various tasks like opening websites, playing music, providing AI-generated responses, and more.

## Features

- **Voice Commands**: Uses speech recognition to take voice commands.
- **Open Websites**: Opens popular websites like YouTube, Wikipedia, Google, and Instagram based on voice commands.
- **Play Music**: Plays a specific music file from your local machine.
- **AI Responses**: Uses OpenAI's API to generate responses to user queries.
- **Time Announcement**: Tells the current time on request.
- **Reset Chat**: Clears the conversation history for a fresh start.
- **Open Applications**: Opens specific applications on your machine like DaVinci Resolve.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/JARVIS-AI.git
    cd JARVIS-AI
    ```

2. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key in the `config.py` file:
    ```python
    apikey = "your_openai_api_key"
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Interact with JARVIS using voice commands.

## Project Structure

``` bash

JARVIS-AI/
│
├── Openai/
│ └── [Generated AI response files will be stored here]
│
├── .gitignore
├── README.md
├── main.py
├── bolo.py
├── config.py
└── requirements.txt

```

## Inspiration

This project is inspired by J.A.R.V.I.S. (Just A Rather Very Intelligent System), the AI assistant from the Iron Man movies and comics. The goal is to create a similar voice-activated assistant with practical applications using modern AI technologies, I took help from Code with Harry's video.
