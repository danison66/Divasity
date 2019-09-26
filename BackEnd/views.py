from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')

    else:
        form = RegisterForm()
    return render(request, 'BackEnd/register.html', {'form':form})




def login(request):
    return render(request, 'BackEnd/login.html')
