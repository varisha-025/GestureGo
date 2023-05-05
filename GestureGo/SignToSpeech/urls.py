from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    # path('login/',views.loginUser,name="login"),
    # path('logout/',views.logoutUser,name="logout"),
    # path('register/',views.registerUser,name="register"),
    # path('privacy/', views.privacy, name='privacy'),
    
]
