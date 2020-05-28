from django.urls import path

from . import views

app_name = 'crypto'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]