from django.urls import path
from .views import RegView, MainView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('reg/', RegView.as_view(), name='reg'),
    path('log/', LoginView.as_view(template_name='registration/log.html'), name='log'),
    path('logout/', LogoutView.as_view(), name='logout'),
]