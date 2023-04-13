from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def registerUser(request):
    if request.user.is_authenticated:
        print("REDERICETED")
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password1')
            email = request.POST.get('email')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            form = UserCreationForm()
        context = {'form':form}
        return render(request, 'register.html', context)
 
   
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username= request.POST.get("username")
            password= request.POST.get("password")
            user_exist = User.objects.filter(username=username).exists()
            print(user_exist)
            user = authenticate(request,username=username, password=password)
            if user is not None and user_exist:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, 'Wrong username or password')
                return render(request,'login.html')
        return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def privacy(request):
    return render(request,'privacy.html')

def logoutUser(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")