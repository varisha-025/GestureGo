from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password1')
            email = request.POST.get('email')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Account was created for ' + username)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
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
    
            user = authenticate(request,username=username, password=password)
            if user is not None and user_exist:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, 'Wrong username or password')
                return render(request,'login.html')
        return render(request,'login.html')
    


def home(request):
    return render(request, 'home.html')

def privacy(request):
    return render(request,'privacy.html')

@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")