from django.urls import path
from django.conf import settings
from django.conf.urls import static
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('registro', views.registro, name='registro'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('contacto',views.contacto,name='contacto'),
    path('perfil', views.perfil, name='perfil'),
    path('perfil/<str:username>', views.perfil, name='perfil'),
    path('comunidad',views.comunidad,name='comunidad'),
    path('publicar',views.publicar, name='publicar'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('unfollow/<str:username>', views.unfollow, name='unfollow'),
]