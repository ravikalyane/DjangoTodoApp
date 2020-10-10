from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='tasks'),
    path('home/', views.home, name='home'),
    path('update/<str:pk>', views.update_task, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('complete/<str:pk>', views.complete, name='complete'),
    path('register/', views.register, name='register'),
    # Password Change urls
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),

]
