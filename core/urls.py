from django.urls import path
from . import views
    
urlpatterns = [

    path('', views.home, name="home"),
    path('about-me/', views.about , name="about"),
    path('store/', views.store , name="store"),
   


]