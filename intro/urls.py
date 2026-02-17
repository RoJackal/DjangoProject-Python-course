from intro import views
from django.urls import path

urlpatterns = [
    path('welcome/', views.welcome_message, name='welcome'),
    path('back/', views.welcome_back, name='back'),
    path('it_innovo/', views.it_innovations, name='innovo'),
    path('top_programming_languages/', views.top_programming_languages, name='top-programming-languages'),
]
