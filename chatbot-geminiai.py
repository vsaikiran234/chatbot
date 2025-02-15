import sys
import google.generativeai as genai
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt

# Set your Gemini API key here
genai.configure(api_key="AIzaSyAJkVVbh9biwkTPPZfAf5F8AqS3Z8AloKQ")

class ChatBot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gemini AI ChatBot")
        self.setGeometry(100, 100, 500, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

    def send_message(self):
        user_input = self.input_field.text().strip()
        if user_input:
            self.chat_display.append(f"You: {user_input}")
            self.input_field.clear()
            
            response = self.get_response(user_input)
            self.chat_display.append(f"Bot: {response}")

    def get_response(self, user_input):
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_input)
            return response.text.strip() if response.text else "No response received."
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBot()
    window.show()
    sys.exit(app.exec_())
