# Django Gemini Chatbot

A web-based chatbot application built with Django that leverages the Gemini API for AI-powered conversational responses. This project provides a clean, interactive interface for users to chat with the bot, including code highlighting and copy-to-clipboard features.

---

## Features

- **Conversational AI:** Uses Gemini API to generate intelligent responses.
- **Modern UI:** Clean, responsive chat interface with code highlighting.
- **Copy Code:** Easily copy code snippets from bot responses.
- **AJAX Chat:** Seamless, real-time chat experience without page reloads.

---

## Project Structure

```
chatbot_project/
├── chatbot/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── chatbot/
│           └── home.html
├── chatbot_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

- **chatbot_project/**: Django project configuration and entry point.
- **chatbot/**: Main app containing chatbot logic, views, and templates.
- **templates/chatbot/home.html**: Main chat UI template.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd chatbot_project
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install django google.generativeai
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

---

## Usage

- Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Type your message in the input box and press "Go".
- The chatbot will respond using the Gemini API.

---

## Configuration

- Ensure you have a valid Gemini API key.
- Update the `api_key` variable in [`chatbot/views.py`](chatbot/views.py) with your actual API key:
  ```python
  api_key = 'YOUR_GEMINI_API_KEY'
  ```

---

## File Highlights

- [`chatbot/views.py`](chatbot/views.py): Handles chat requests and integrates with Gemini API.
- [`chatbot/templates/chatbot/home.html`](chatbot/templates/chatbot/home.html): Frontend chat interface with AJAX and code highlighting.

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss any major changes.

---

## License

This project is for educational purposes. Please check Gemini API terms for commercial use.
