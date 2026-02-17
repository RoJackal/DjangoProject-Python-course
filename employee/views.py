import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from employee.forms import EmployeeForm, EmployeeUpdateForm
from employee.models import Employee
# CreateView - o clasa generica implementata de Django folosit pentru a salva datele dintr-un formular in baza de date


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	template_name = 'employee/create_employee.html'  # calea catre fisierul html unde va fi implementat formularul
	model = Employee  # pentru definirea formularul in interfata, implicit salvarea datelor
	form_class = EmployeeForm
	success_url = '/list_employees/'  # in momentul salvarii datelor din formular utilizatorul va fi redirectionat pe pagina specificata aici
	permission_required = 'employee.add_employee'
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		
		now = datetime.datetime.now()
		context['current_datetime'] = now
		
		active_employees = Employee.objects.filter(active=True)
		context['active_employees'] = active_employees
		
		return context
# ListView - o clasa generica implementata de Django folosita pentru a afisa datele dintr-un model/dintr-o baza de date
class EmployeeListView(LoginRequiredMixin, ListView):
	template_name = 'employee/list_of_employees.html'
	model = Employee
	context_object_name = 'all_employees'  # Employee.objects.all()
	def get_queryset( self ):
		return Employee.objects.filter(active=True)
	def get_context_data( self, **kwargs ):
		context = super().get_context_data(**kwargs)
		
		no_of_employees = Employee.objects.filter(active=True).count()
		context['no_of_employees'] = no_of_employees
		
		return context
# UpdateView- o clasa generica implementata de Django pentru a actualiza un obiect pe baza unui formular
class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'employee/update_employee.html'
	model = Employee
	form_class = EmployeeUpdateForm
	success_url = '/list_employees/'
# DeleteView - o clasa generica implementata de Django pentru stergea unui obiect din baza de date dintr-o specifica specifica
class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'employee/delete_employee.html'
	model = Employee
	success_url = '/list_employees/'
# DetailView - o clasa generica implementata de Django pentru a afisa informatiile unui obiect
class EmployeeDetailView(LoginRequiredMixin, DetailView):
	template_name = 'employee/details_employee.html'
	model = Employee
