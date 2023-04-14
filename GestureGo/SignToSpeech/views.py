from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .utils.googletranslate import GoogleTranslate


@login_required(login_url='login')
def dashboard(request):
    return render(request,'sign_to_speech/dashboard.html')

@login_required(login_url='login')
def prediction(request):
    return JsonResponse({"message": "ok"})






# use this as a utility function
# def convert_english_text_to_speech():
#     pass

# use this as a utility function
# def get_text_in_english():
#     res = None
#     eng_res = GoogleTranslate.translate_to_en(res)
#     speech = convert_english_text_to_speech(eng_res)
#     return JsonResponse({"message": eng_res, "speech": speech})

def page_not_found(request,exception):
    return render(request,'sign_to_speech/404.html')