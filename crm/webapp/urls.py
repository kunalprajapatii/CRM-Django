from django.urls import path, include
from webapp.views import *

urlpatterns = [
    path('',home,name="home"),
    path('register',register,name="register"),
    path('my-login',my_login,name="my-login"),
    path('user-logout',user_logout,name="user-logout"),
    path('dashboard',dashboard,name="dashboard"),
    path('create-record',create_record,name="create-record"),
    path('update-record/<int:pk>',update_record,name="update-record"),
    path('delete-record/<int:pk>',delete_record,name="delete-record"),
    path('record/<int:pk>',single_record,name="record"),
    

]