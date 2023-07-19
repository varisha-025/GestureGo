from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import JsonResponse

from .utils.googletranslate import GoogleTranslate



def signtospeech(request):
    return render(request, 'signtospeech.html')


# @login_required(login_url='login')
# def prediction(request):
#     return JsonResponse({"message": "ok"})

# # use this as a utility function
# def convert_english_text_to_speech():
#     pass

# # use this as a utility function
# def get_text_in_english():
#     res = None
#     eng_res = GoogleTranslate.translate_to_en(res)
#     speech = convert_english_text_to_speech(eng_res)
#     return JsonResponse({"message": eng_res, "speech": speech})