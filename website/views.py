from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUp



def home(request):
    #check if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again.")
            return redirect('home')
    else:    
        return render(request, 'home.html', {})

#def log_in(request):
    pass

def log_out(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect('home')

def registration(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered, welcome!")
            return redirect('home')
    else:
        form = SignUp()
    return render(request, 'register.html', {'form':form})

