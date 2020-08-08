from django.urls import path
from .views import *

urlpatterns = [
    # path('', HeaderInfo.as_view(), name='home'),
    path('', index, name = 'home'),
    path('infirmation/<int:pk>', information, name='information'),
]
