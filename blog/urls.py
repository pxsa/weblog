from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.say_hi, name='say_hi'),
    path('', views.all, name='all_posts')
]