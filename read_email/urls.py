from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import OrderViewSet
from read_email.email_parser import read_gmail


router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('read-emails/', read_gmail),
    path('', include(router.urls)),
]
