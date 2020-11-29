from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('events/',views.events,name="events"),
    path('create', views.create, name='create'),
    path('math/', views.math, name="math"),
    path('course', views.course, name='1 course'),
    path('course2', views.coursee, name='2 course'),
    path('helpers/', views.helpers, name="helpers"),

]
