from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from SignToSpeech.forms import RegisterForm, LoginForm


def loginUser(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                print("login")
                login(request, user)
                return redirect("menu")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("home")

        print(form.errors)
        return render(request, 'login.html', {"form": form})
    else:
        return redirect("login")

def registerUser(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        print("post")
        if form.is_valid():
            print("valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("register")

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("register")

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            print("user created")
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("login")
        print("invalid")
        print(form.errors)
    else:
        return render(request, "register.html", {"form": form})
        

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login")
  
def privacy(request):
    return render(request,'privacy.html')

def asl(request):
    return render(request,'asl.html')

def translation(request):
    return render(request, 'translation.html')

def menu(request):
    return render(request, 'layout/menu.html')

def text_to_speech(request):
    return render(request, 'text_to_speech.html')

def speech_to_sign(request):
    return render(request, 'speech_to_sign.html')

def home(request):
    return render(request, 'layout/home.html')


def speech_to_sign(request):
	if request.method == 'POST':
		text = request.POST.get('sen')
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)

		tagged = nltk.pos_tag(words)
		tense = {}
		tense["future"] = len([word for word in tagged if word[1] == "MD"])
		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])



		#stopwords that will be removed
		stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])



		#removing stopwords and applying lemmatizing nlp process to words
		lr = WordNetLemmatizer()
		filtered_text = []
		for w,p in zip(words,tagged):
			if w not in stop_words:
				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
					filtered_text.append(lr.lemmatize(w,pos='v'))
				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
					filtered_text.append(lr.lemmatize(w,pos='a'))

				else:
					filtered_text.append(lr.lemmatize(w))


		#adding the specific word to specify tense
		words = filtered_text
		temp=[]
		for w in words:
			if w=='I':
				temp.append('Me')
			else:
				temp.append(w)
		words = temp
		probable_tense = max(tense,key=tense.get)

		if probable_tense == "past" and tense["past"]>=1:
			temp = ["Before"]
			temp = temp + words
			words = temp
		elif probable_tense == "future" and tense["future"]>=1:
			if "Will" not in words:
					temp = ["Will"]
					temp = temp + words
					words = temp
			else:
				pass
		elif probable_tense == "present":
			if tense["present_continuous"]>=1:
				temp = ["Now"]
				temp = temp + words
				words = temp


		filtered_text = []
		for w in words:
			path = w + ".mp4"
			f = finders.find(path)
			#splitting the word if its animation is not present in database
			if not f:
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text;


		return render(request,'speech_to_sign.html',{'words':words,'text':text})
	else:
		return render(request,'speech_to_sign.html')