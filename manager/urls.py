from django.urls import path

from manager import views

urlpatterns = [
    path('create_manager/', views.ManagerCreateView.as_view(), name='create-manager'),
    path('list_managers/', views.ManagerListView.as_view(), name='list-managers'),
]