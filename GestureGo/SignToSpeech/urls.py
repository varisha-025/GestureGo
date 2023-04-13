from django.urls import path
from . import views

urlpatterns = [
     path('',views.dashboard,name="dashboard"),
     path('prediction/',views.prediction,name="prediction"),
     path('result/',views.result,name="result"),
]

handler404 = "SignToSpeech.views.page_not_found"