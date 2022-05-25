from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import MainHome, PostDetailView, SignUpView, SignInView, FeedbackView, SuccessView, SearchResultsView, TagView
from django.conf import settings

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('home/<slug:slug>/', PostDetailView.as_view(), name='detail_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/', FeedbackView.as_view(), name='contact'),
    path('contact/success', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
]




