from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from manager.forms import ManagerForm
from manager.models import Manager


class ManagerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'manager/create_manager.html'
    model = Manager
    form_class = ManagerForm
    success_url = '/'

class ManagerListView(LoginRequiredMixin, ListView):
    template_name = 'manager/list_of_managers.html'
    model = Manager
    context_object_name = 'all_managers'
