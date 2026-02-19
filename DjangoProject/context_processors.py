from django.core.cache import cache
from employee.models import Employee
def get_all_employees( request ):
	"""
    Context processor to provide employee data globally.
    Optimized with caching and efficient query.
    """
	# Try to get from cache first
	cache_key = 'context_employees_data'
	cached_data = cache.get(cache_key)
	
	if cached_data is not None:
		return cached_data
	
	# Query database with optimization
	employees_queryset = Employee.objects.filter(active=True).select_related('manager')
	total_count = employees_queryset.count()
	
	# Get only first 3 employees
	employees_list = list(employees_queryset[:3])
	
	data = {
		'employees':       employees_list,
		'no_of_max':       total_count > 3,
		'total_employees': total_count,
		}
	
	# Cache for 5 minutes
	cache.set(cache_key, data, 300)
	return data
