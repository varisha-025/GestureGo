from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('privacy/', views.privacy, name='privacy'),
    
]

handler404 = "SignToSpeech.views.page_not_found"