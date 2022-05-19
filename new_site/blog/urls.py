from django.urls import path, include
from . import views
from .views import MainHome


urlpatterns = [
    path('', MainHome.as_view(), name='home'),
]


