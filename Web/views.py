from django.shortcuts import render, redirect
from Exam.models import professeur
from django.contrib import messages
from django.contrib.auth.views import auth_login
# Create your views here.

def home(request):
    return render(request, 'interfaces/Accueil.html', {'A': '10'})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('mdp')
        num = professeur.objects.filter(email=email).count()
        print(num)
        if num == 0:
            messages.info(request, 'Ce compte n\'existe pas')
            return redirect('login')
        elif num != 0 :
            A = professeur.objects.get(email=email)
            if  password != A.password:
                messages.info(request, 'mot de passe incorrect')
                return redirect('login')
            elif password == A.password:
                return redirect('exam')
                messages.info(request, 'vous avez connecté')
    else:
        return render(request, 'interfaces/login.html')



def signup(request):
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    email = request.POST.get('email')
    password = request.POST.get('mdp1')
    passwordc = request.POST.get('mdp2')
    departement = request.POST.get('dept')
    if request.method == 'POST':
        if password==passwordc:
            if professeur.objects.filter(email=email):
                messages.info(request,'Email déjà exist essayer un autre')
                return redirect('signup')
            else:
                data = professeur(nom = nom, prenom =prenom, email = email, password = password, departement =departement)
                data.save()
                messages.info(request, 'You are successfully signUp')
                return redirect('login')
        else:
            messages.info(request, 'Le mot de passe non confirmée')
            return redirect('signup')

    return render(request, 'interfaces/signup.html')
