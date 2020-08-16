from django.urls import path
from .views import *

urlpatterns = [
    # path('', HeaderInfo.as_view(), name='home'),
    path('', Home.as_view(), name = 'home'),
    path('infirmation/<int:pk>/', Information.as_view(), name='information'),
    path('spezialization/<int:specialization_id>/', SpecDoctor.as_view(), name= 'specialization'),
    path('discounts/<int:pk>/', Discount.as_view(), name = 'discounts'),
    path('doctor_detail/<int:pk>/', ViewDoctor.as_view(), name = 'view_doctor'),
    path('article/<int:pk>', ViewArticle.as_view(), name = 'article_detail' )
]
