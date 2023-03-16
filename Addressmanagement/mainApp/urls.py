from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    # path('post/<int:pk>/', views.post_python manage.py makemigrationsdetail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]