from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import MainHome, PostDetailView, SignUpView, SignInView
from django.conf import settings

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('home/<slug>/', PostDetailView.as_view(), name='detail_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
]
