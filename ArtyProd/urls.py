from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('team', views.Team, name='team'),
    path('login1', views.login1, name='login1'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('demande', views.create_demande, name='demande'),
    path('projets', views.projets, name='projets'),
    path('demande_detail', views.demande_detail, name='demande_detail'),
    path('project_detail', views.project_detail, name='project_detail')
   
]
