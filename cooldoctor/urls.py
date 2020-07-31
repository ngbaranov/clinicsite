from django.urls import path
from .views import *

urlpatterns = [
    path('', HeaderInfo.as_view(), name='home')
]