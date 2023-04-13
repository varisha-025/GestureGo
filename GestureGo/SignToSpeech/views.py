from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse


def dashboard(request):
    return render(request,'sign_to_speech/dashboard.html')


def prediction(request):
    return JsonResponse({"message": "ok"})

def result(request):
    return JsonResponse({"message": "ok"})


def page_not_found(request,exception):
    return render(request,'sign_to_speech/404.html')