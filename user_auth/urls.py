from django.urls import path
from . import views



app_name = 'user_auth'
urlpatterns = [
    path('',views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('user/',views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
]
