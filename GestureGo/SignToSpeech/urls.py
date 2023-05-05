from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('privacy/', views.privacy, name='privacy'),
    
]

# handler404 = "SignToSpeech.views.page_not_found"