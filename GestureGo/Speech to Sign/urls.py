from django.urls import path

from . import views

urlpatterns = [
    path('', views.signtospeech, name='signtospeech'),
]
