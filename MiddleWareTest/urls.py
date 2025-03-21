from django.urls import path
from .views import *

urlpatterns = [
    path("middleware_test", middleware_test),
]