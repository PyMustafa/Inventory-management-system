from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
