from django.urls import path

from . import views

urlpatterns = [
    # path('', views.all, name='all_posts'), 
    path('', views.PostList.as_view(), name='all_posts'), 

    # path('detail/<int:pk>', views.detail, name='post_detail'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),

    path('create/', views.create_post, name='create_post'),
    path('update/<int:pk>', views.update_post, name='update_post'),
    path('delete/<int:pk>', views.remove_post, name='remove_post'),
]