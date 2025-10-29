# Gemini AI Chatbot

A Streamlit chat UI for the Google Gemini API that now keeps your chat history on disk for quick restarts and review.

## Features

- Streaming responses from the `gemini-2.5-flash` model using the `google-genai` SDK.
- Session and local persistence: chat history is cached in Streamlit session state and saved to `chat_history.json` for reuse across runs.
- Simple separation of concerns: `chatbot_api.py` isolates Gemini client setup and streaming helpers used by `app.py`.
- Environment-driven configuration via `.env`, keeping secrets out of source control.

## Project layout

- `app.py` – Streamlit UI, history handling, and user interaction.
- `chatbot_api.py` – Gemini client initialization plus chat helpers.
- `chat_history.json` – Generated file that stores the most recent conversation.
- `requirements.txt` – Python dependencies.

## Prerequisites

- Python 3.8+ (3.10+ recommended).
- A Google Gemini API key with access to the `gemini-2.5-flash` (or compatible) model.

## Quick start (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
echo GEMINI_API_KEY=your_api_key_here > .env
streamlit run app.py
```

Replace `your_api_key_here` with your actual key. The `python-dotenv` package loads this value when the app starts.

## Usage

- Open the Streamlit page, type a prompt, and watch the assistant respond in real time.
- Each user/assistant exchange is mirrored to `chat_history.json`. The file is recreated automatically if deleted.
- Select **🧹 Clear Chat** in the UI to reset both the session history and the saved JSON file.
- Change the default model by editing the `model_name` parameter in `create_chat_session` inside `chatbot_api.py`.

## Troubleshooting

- If imports fail, confirm the virtual environment is active and dependencies were installed without errors.
- If authentication fails, double-check the `GEMINI_API_KEY` in `.env` and ensure your account has access to the specified model.
- Delete `chat_history.json` if it becomes corrupted; a fresh file will be created on the next message.

## License

This project currently has no explicit license (add one before distributing or publishing).
