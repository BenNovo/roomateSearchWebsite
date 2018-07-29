from django.urls import include, path

from . import views

urlpatterns = [    
    path('loginP/', views.logIn, name='loginP'),
    path('createUserP/', views.createUser, name='createUserP'),
    path('', views.index, name='index'),
]
