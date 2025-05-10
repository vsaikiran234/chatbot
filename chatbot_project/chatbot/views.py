from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

def home(request):
    return render(request, 'chatbot/home.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        api_key = 'AIzaSyAJkVVbh9biwkTPPZfAf5F8AqS3Z8AloKQ'  # Replace with your actual API key
        genai.configure(api_key=api_key)
        try:
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(user_input)
            answer = response.text.strip() if response.text else "No response received."
        except Exception as e:
            answer = f"Error: {str(e)}"
        return JsonResponse({'response': answer})