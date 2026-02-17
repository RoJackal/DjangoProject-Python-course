from employee.models import Employee


def get_all_employees(request):
    return {
        'employees': Employee.objects.all()[:3] if Employee.objects.count() > 3 else Employee.objects.all(),
        'no_of_max': True if Employee.objects.all().count() > 3 else False,
    }