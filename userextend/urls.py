from django.urls import path
from django.contrib.auth import views as auth_views
from userextend import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='userextend/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
