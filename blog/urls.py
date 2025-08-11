from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/edit/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]
