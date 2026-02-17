import datetime
import logging

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy

from DjangoProject.settings import DEFAULT_FROM_EMAIL
from userextend.forms import SignUpForm
from userextend.models import Logs
logger = logging.getLogger(__name__)
class UserCreateView(CreateView):
	"""Create new user with email notification"""
	template_name = 'userextend/create_user.html'
	model = User
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	def form_valid( self, form ):
		"""Process form and send welcome email"""
		if form.is_valid():
			try:
				# 1. Modify data before saving
				new_user = form.save(commit=False)
				new_user.first_name = new_user.first_name.title()
				new_user.last_name = new_user.last_name.title()
				new_user.save()
				
				# 2. Add log entry
				log_text = f"{new_user.first_name} {new_user.last_name} was successfully registered"
				Logs.objects.create(text=log_text, created=datetime.datetime.now())
				logger.info(log_text)
				
				# 3. Send welcome email
				try:
					title = 'Welcome to DjangoProject'
					content = (
						f"Hello {new_user.first_name} {new_user.last_name}!\n\n"
						f"Your account has been created successfully!\n\n"
						f"Username: {new_user.username}\n"
						f"Email: {new_user.email}\n\n"
						f"Please login to continue."
					)
					
					send_mail(
							subject=title,
							message=content,
							from_email=DEFAULT_FROM_EMAIL,
							recipient_list=[new_user.email],
							fail_silently=False,
							)
					logger.info(f'Welcome email sent to {new_user.email}')
				
				except Exception as e:
					# Log email error but don't fail user creation
					logger.error(f'Failed to send welcome email to {new_user.email}: {str(e)}')
					messages.warning(
							self.request,
							'Account created but welcome email could not be sent.'
							)
				
				messages.success(self.request, 'Account created successfully! Please login.')
			
			except Exception as e:
				logger.error(f'Error creating user: {str(e)}')
				messages.error(self.request, 'An error occurred during registration.')
				raise
		
		return super().form_valid(form)
	def form_invalid( self, form ):
		"""Handle invalid form submission"""
		messages.error(self.request, 'Please correct the errors below.')
		return super().form_invalid(form)
