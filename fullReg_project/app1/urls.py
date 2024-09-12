from django.urls import path
from . import views
urlpatterns = [
    path('',views.signupPage,name='signupPage'),
    path('login/',views.loginPage,name='loginPage'),
    path('home/',views.homePage,name='homePage'),
    path('logout/',views.logoutPage,name='logoutPage')
]