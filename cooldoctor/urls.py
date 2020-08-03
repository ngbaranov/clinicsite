from django.urls import path
from .views import *

urlpatterns = [
    path('', HeaderInfo.as_view(), name='home'),
    path('topmenu/<int:pk>', ViewTopmenu.as_view(), name='topmenu'),
]
