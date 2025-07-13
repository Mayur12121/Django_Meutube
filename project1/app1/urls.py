from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',  auth_views.LoginView.as_view(template_name='registration/login.html'),  name='login'),
    path('abc_list', views.abc_list, name='abc_list'),
    path('create/', views.list_create, name='list_create'),
    path('<int:id>/edit/', views.list_edit, name='list_edit'),
    path('<int:id>/delete/', views.list_delete, name='list_delete'),
    path('register/', views.register, name='register'),
    path('accounts/login/',  auth_views.LoginView.as_view(template_name='registration/login.html'),  name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='abc_list'), name='logout'),
    path('play-video/<int:id>/', views.play_video, name='play_video'),
]
