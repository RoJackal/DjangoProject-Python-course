from django.urls import path
from employee import views

urlpatterns = [
    path('create/', views.EmployeeCreateView.as_view(), name='create_employee'),
    path('list/', views.EmployeeListView.as_view(), name='list_employees'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('details/<int:pk>/', views.EmployeeDetailView.as_view(), name='details_employee'),
]
