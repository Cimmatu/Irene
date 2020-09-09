from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
