# README.md

# Chatbot Project

This is a Django-based chatbot project that provides an interface for users to interact with a chatbot powered by the Gemini API.

## Project Structure

The project is organized as follows:

```
chatbot_project
├── chatbot
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chatbot_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot_project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django google.generativeai
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the chatbot interface.
- Use the input field to send messages to the chatbot and receive responses.

## Configuration

- Ensure that the `google.generativeai` library is installed and configured properly in your Django environment.
- Update the `api_key` in the `generate_gemini_response` function within `views.py` to use your actual API key.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.