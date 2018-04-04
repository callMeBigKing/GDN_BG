from django.urls import path

from . import views

app_name = 'usermsg'

urlpatterns = [

    path('user_msg/', views.user_msg, name='user_msg'),

    path('signin/', views.signin, name='signin'),

    path('login/', views.login, name='login'),

    path('<int:user_id>/user_msg_change/', views.user_msg_change, name='user_msg_change')
]