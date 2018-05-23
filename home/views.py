from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from home.form import SignUpForm



def homepage(request):
    return render(request, 'home/starting_page.html')

def baseone(request):
    return render(request, 'home/base.html')

def index(request):
    return render(request, 'home/index.html')

def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
    else:
        form = SignUpForm()

    return render(request, 'home/registration.html', {'form':form })