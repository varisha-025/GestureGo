from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse


def dashboard(request):
    return JsonResponse({"message": "ok"})