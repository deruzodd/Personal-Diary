from django.urls import path
from . import views
from django.contrib.auth import views as viewsAuth

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', viewsAuth.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', viewsAuth.LogoutView.as_view(), name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('settings/', views.user_config, name='user_config'),
    path('demo/', views.demo_login, name='demo_login'),
]
