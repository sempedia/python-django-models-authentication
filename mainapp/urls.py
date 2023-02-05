from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:id>', views.post, name='post'),
#    path('user/<int:id>', views.user_posts, name='user_posts'),
#    path('tag/<str:name>', views.tag_posts, name='tag_posts'),
    path('', views.index, name='index'),
    path('tag/<str:name>', views.tag_posts, name='tag_posts'),
] 