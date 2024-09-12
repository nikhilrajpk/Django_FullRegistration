from django.shortcuts import render

# Create your views here.
def signupPage(request):
    return render(request,'signup.html')

def loginPage(request):
    return render(request,'login.html')

def homePage(request):
    return render(request,'home.html')