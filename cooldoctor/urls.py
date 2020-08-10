from django.urls import path
from .views import *

urlpatterns = [
    # path('', HeaderInfo.as_view(), name='home'),
    path('', Home.as_view(), name = 'home'),
    path('infirmation/<int:pk>/', information, name='information'),
    path('spezialization/<int:specialization_id>/', specialization, name= 'specialization')
]
