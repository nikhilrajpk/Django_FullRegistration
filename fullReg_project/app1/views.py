from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.
@never_cache
def signupPage(request):
    # if request.method == 'POST':
    #     form = CustomForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    #         messages.success(request,'Your account has been created ')
    #         return redirect(loginPage)
    # else:
    #     form = CustomForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('loginPage')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request,'signup.html',{'form':form})

@never_cache
def loginPage(request):
    if request.method == 'POST':
        pass
    return render(request,'login.html')

@never_cache
def homePage(request):
    return render(request,'home.html')

@never_cache
def logoutPage(request):
    return redirect(loginPage)