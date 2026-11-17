
# DNA - Intelligent Personal AI Assistant

DNA is an AI-powered personal voice assistant designed
to provide natural, real-time human-like conversations.

Built using Python, LiveKit and Google's Gemini
Realtime API, DNA enables users to interact with an
AI assistant through voice.

## Features

- Real-time voice interaction
- Natural conversational responses
- Gemini-powered AI intelligence
- Low-latency voice communication
- Continuous conversational sessions
- Context-aware conversations
- Python-based implementation

## Technology Stack

- Python
- LiveKit Agents
- LiveKit Google Plugin
- Google Gemini Realtime API
- python-dotenv

## Project Structure

DNA/
├── agent.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Prerequisites

- Python 3.10+
- Google Gemini API key
- Internet connection
- Microphone and speakers

## Installation

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/DNA-Intelligent-Personal-AI-Assistant.git

Navigate to the project:

    cd DNA-Intelligent-Personal-AI-Assistant

Create a virtual environment:

    python -m venv agent

Activate it on Windows:

    .\agent\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

## Configuration

Create a `.env.local` file in the project root.

Add your Gemini API key:

    GOOGLE_API_KEY=your_api_key

Never publish your actual API key.

## Run the Assistant

    python agent.py console

## Future Enhancements

- Long-term conversational memory
- Web search integration
- Desktop automation
- Offline AI capabilities
- Proactive personal assistance
- Application and system control

## Author

Praveen J

## License

MIT License
