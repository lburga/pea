from django.urls import path, include
from apps.demo.views import (login, main,)

app_name = 'demo'

urlpatterns = [
    path('', login, name='login'),
    path('main/', main, name='main'),

]
