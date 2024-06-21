from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.say_hi, name='say_hi'),
    path('', views.all, name='all_posts'), 
    path('detail/<int:post_id>', views.detail, name='post_detail'),

    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>', views.update_post, name='update_post'),
    path('delete/<int:post_id>', views.remove_post, name='remove_post'),
]