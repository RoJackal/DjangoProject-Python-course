from django.urls import path

from manager import views

urlpatterns = [
    path('view_profile/<int:manager_id>/', views.view_profile, name='view_profile'),
    path('create_manager/', views.ManagerCreateView.as_view(), name='create_manager'),

    path('list_managers/', views.ManagerListView.as_view(), name='list_managers'),
    path('view_profile/<int:manager_id>/', views.view_profile, name='view_profile'),
]
