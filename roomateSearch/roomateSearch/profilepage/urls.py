from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('changeS/', views.changeSurvey, name='changeS'),
    url(r'^profileP/<pk>/$', views.profileP),
    url(r'^changeS/$', views.changeSurvey),
    path('profileP/<pk>/', views.profileP, name='profileP'),
    #path('', views.profileP, name='profileP'),
]
