from django.urls import path

from . import views

urlpatterns = [
	path('singup/', views.SignUpView.as_view(), name='signup'),
]