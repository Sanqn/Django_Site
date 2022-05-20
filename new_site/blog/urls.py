from django.urls import path, include
from . import views
from .views import MainHome, PostDetailView


urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('home/<slug>', PostDetailView.as_view(), name='detail_page'),
]


