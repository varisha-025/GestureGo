from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User

# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
# from .forms import UserRegisterForm





def signup(request):
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     print('post')
    #     if form.is_valid():
    #         print('form is valid')
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         email = form.cleaned_data.get('email')

    #         messages.success(request, f'{username}, Your account has been created! You are now able to log in')
    #         return redirect('login')
    #     else:
    #         print('form is not valid')
    #         messages.error(request, f'Please correct the errors below')
    # print('get')
    # form = UserCreationForm()
    # return render(request, 'signup.html', {'form': form, 'title':'Sign up'})
    form=UserCreationForm()
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid:
            user=User.objects.create(form)
            form.save()
    context ={'form':form}
    return render(request , 'signup.html' ,context)   
     
def login(request):
    if request.user.is_authenticated:
        print("auth done")
        return redirect('/')
    else:
        if request.method == 'POST':
            print('post')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                print('user is not none')
                form = login(request, user)
                messages.success(request, f'Welcome {username} !!')
                return redirect('/')
            else:
                messages.info(request, f'This account does not exist')
        
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'Login page'})


# Create your views here.

def home(request):
    return render(request, 'home.html')




def privacy(request):
    return render(request,'privacy.html')
def logout(request):
    pass
    # return render(request, 'logout.html')