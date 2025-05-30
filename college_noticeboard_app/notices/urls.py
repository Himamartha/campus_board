from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('notice/create/', views.notice_create, name='notice_create'),
    path('notice/<int:pk>/edit/', views.notice_edit, name='notice_edit'),
    path('notice/<int:pk>/delete/', views.notice_delete, name='notice_delete'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
] 