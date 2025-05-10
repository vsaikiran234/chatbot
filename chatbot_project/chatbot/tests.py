# File: /chatbot_project/chatbot_project/chatbot/tests.py

from django.test import TestCase
from django.urls import reverse

class ChatbotViewsTests(TestCase):

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_response_view_status_code(self):
        response = self.client.post(reverse('get_response'), {'user_input': 'Hello'})
        self.assertEqual(response.status_code, 200)

    def test_get_response_view_invalid_data(self):
        response = self.client.post(reverse('get_response'), {})
        self.assertEqual(response.status_code, 400)