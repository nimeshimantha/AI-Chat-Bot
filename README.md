# Gemini AI Chatbot

A small Streamlit app that connects to Google Gemini (GenAI) to provide a streaming chat interface.

## What this is

- `app.py` is a Streamlit-based chat UI that sends user prompts to a Gemini model and displays streaming responses.

## Prerequisites

- Python 3.8+ (3.10+ recommended)
- A Google Gemini (GenAI) API key with access to the model used by the app.

## Installation (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the project root containing your API key:

```
GEMINI_API_KEY=your_api_key_here
```

Note: `app.py` uses `python-dotenv` to load the `GEMINI_API_KEY` environment variable.

## Run the app

Start the Streamlit app:

```powershell
streamlit run app.py
```

This opens a browser UI where you can type prompts and receive streaming responses from the Gemini model.

## Troubleshooting

- If you get import errors, ensure your virtual environment is activated and `pip install -r requirements.txt` completed without errors.
- If the Gemini connection fails, verify your `GEMINI_API_KEY` and check network/firewall restrictions.

## Notes

- The code stores chat history in the Streamlit session state only (no persistent storage).
- The code uses the `gemini-2.5-flash` model in `app.py`; change the model name there if needed.

## License

This project has no explicit license (add one if you intend to publish it).
