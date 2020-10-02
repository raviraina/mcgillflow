from django.urls import path
from django.conf.urls import url
from . import views
from website.views import home, search
urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
]
