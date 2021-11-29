from django.contrib import admin
from django.urls import path
from Service.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='home'),
    path('sign_in', Sign_in.as_view(), name='Sing_In'),
    path('sign_up', Sign_up.as_view(), name='Sign-Up'),
    path('start_path', Start.as_view(), name='Start_path'),
    path('history_list', History_payments.as_view(), name='history_list')
]
