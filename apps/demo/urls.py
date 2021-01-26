from django.urls import path, include
from apps.demo.views import (login,)

app_name = 'demo'

urlpatterns = [
    path('', login, name='login'),
]
