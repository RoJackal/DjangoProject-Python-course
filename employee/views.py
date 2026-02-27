import datetime
import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from employee.forms import EmployeeForm, EmployeeUpdateForm
from employee.models import Employee
logger = logging.getLogger(__name__)
class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	"""Create new employee with permission check"""
	template_name = 'employee/create_employee.html'
	model = Employee
	form_class = EmployeeForm
	success_url = reverse_lazy('list_employees')  # FIXED: Changed from 'list_employees'
	permission_required = 'employee.add_employee'
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		context['current_datetime'] = datetime.datetime.now()
		
		# Optimize query with select_related
		active_employees = Employee.objects.filter(active=True).select_related('manager')
		context['active_employees'] = active_employees
		context['active_count'] = active_employees.count()
		
		return context
	def form_valid( self, form ):
		messages.success(self.request, 'Employee created successfully!')
		logger.info(f'Employee {form.instance.full_name} created by {self.request.user}')
		return super().form_valid(form)
	def form_invalid( self, form ):
		messages.error(self.request, 'Error creating employee. Please check the form.')
		return super().form_invalid(form)
class EmployeeListView(LoginRequiredMixin, ListView):
	"""List all active employees with pagination"""
	template_name = 'employee/list_of_employees.html'
	model = Employee
	context_object_name = 'all_employees'
	paginate_by = 25
	def get_queryset( self ):
		"""Optimize query with select_related and only load needed fields"""
		queryset = Employee.objects.filter(active=True).select_related('manager').order_by('-hire_date')
		
		# Add search functionality
		search_query = self.request.GET.get('search', '')
		if search_query:
			queryset = queryset.filter(
					Q(first_name__icontains=search_query) |
					Q(last_name__icontains=search_query) |
					Q(email__icontains=search_query)
					)
		
		return queryset
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		
		# Get count efficiently
		context['no_of_employees'] = self.get_queryset().count()
		context['search_query'] = self.request.GET.get('search', '')
		
		return context
class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	"""Update existing employee"""
	template_name = 'employee/update_employee.html'
	model = Employee
	form_class = EmployeeUpdateForm
	success_url = reverse_lazy('list_employees')  # FIXED: Changed from 'list_employees'
	permission_required = 'employee.change_employee'
	def form_valid( self, form ):
		messages.success(self.request, f'Employee {form.instance.full_name} updated successfully!')
		logger.info(f'Employee {form.instance.full_name} updated by {self.request.user}')
		return super().form_valid(form)
	def form_invalid( self, form ):
		messages.error(self.request, 'Error updating employee. Please check the form.')
		return super().form_invalid(form)
class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	"""Soft delete employee by setting active=False"""
	template_name = 'employee/delete_employee.html'
	model = Employee
	success_url = reverse_lazy('list_employees')  # FIXED: Changed from 'list_employees'
	permission_required = 'employee.delete_employee'
	def delete( self, request, *args, **kwargs ):
		"""Soft delete instead of hard delete"""
		self.object = self.get_object()
		employee_name = self.object.full_name
		
		# Soft delete
		self.object.active = False
		self.object.save()
		
		messages.success(request, f'Employee {employee_name} deactivated successfully!')
		logger.info(f'Employee {employee_name} deactivated by {request.user}')
		
		return super().delete(request, *args, **kwargs)
class EmployeeDetailView(LoginRequiredMixin, DetailView):
	"""Display employee details"""
	template_name = 'employee/details_employee.html'
	model = Employee
	def get_queryset( self ):
		"""Optimize query with select_related"""
		return Employee.objects.select_related('manager')
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		# Add additional context
		employee = self.object
		context['years_employed'] = (datetime.date.today() - employee.hire_date).days // 365
		return context
