"""
URL configuration for DjangoProject project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from userextend.forms import LoginForm
urlpatterns = [
	# Admin
	path('admin/', admin.site.urls),
	# Authentication
	path('login/', auth_views.LoginView.as_view(form_class=LoginForm), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	# App URLs - REMOVED PREFIXES
	path('', include('employee.urls')),  # CHANGED back to empty
	path('', include('manager.urls')),  # CHANGED back to empty
	path('', include('userextend.urls')),  # CHANGED back to empty
	path('', include('intro.urls')),  # CHANGED back to empty
	path('', include('home.urls')),  # Home MUST BE LAST
	]
# Serve media files in development
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
