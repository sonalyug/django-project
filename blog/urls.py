from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),           # /blog/
    path('create/', views.blog_create, name='blog_create'),
    path('view/<int:pk>/', views.blog_view, name='blog_view'),
    path('edit/<int:pk>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
]
