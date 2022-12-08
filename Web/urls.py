from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Log/', views.login, name='login'),
    path('SignUp/', views.signup, name='signup'),
]