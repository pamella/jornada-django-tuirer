# URLs de users
from django.urls import path
from users.views import (
    ProfileEditView,
    ProfileView,
    UserLoginView,
    UserLogoutView,
    UserSignupView,
)

app_name = 'users'

urlpatterns = [
    # indica o tipo e a variável
    # pk do model que será carregado na view passada
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='profile-edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('cadastro/', UserSignupView.as_view(), name='signup'),
]
