from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>', views.post_detail, name='post'),
    path('post_new', views.post_new, name='post_new'),
    path('tags/<tag_slug>/', views.posts_by_tag, name='tags')
]
