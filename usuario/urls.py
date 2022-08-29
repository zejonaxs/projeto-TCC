from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/', PasswordChangeView.as_view(template_name='usuario/mudar_senha.html'), name='password'),
    path('criar/usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('editar/usuario/<int:pk>', UsuarioUpdate.as_view(), name='editar_usuario'),
    path('listar/usuarios/', UsuarioList.as_view(), name='listar_usuarios'),
    path('detalhar/usuario', UsuarioDetail.as_view(), name='detalhar_usuario'),
    path('deletar/usuario/<int:pk>', UsuarioDelete.as_view(), name='deletar_usuario'),
]
