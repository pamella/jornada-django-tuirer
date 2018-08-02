from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# updateview --> usada para editar um model que já existe
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import UserCreationForm
from users.mixins import ProfileAccessMixin
from users.models import User
from users.forms import UserSignupForm


# https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#detailview
# a ordem dos Mixins importa. o quanto antes, maior a importância

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    # alteramos o nome que chamaremos o model no template a partir do context_object_name
    context_object_name = 'profile'


class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username')
    template_name = 'profile_edit.html'
    # success_url = reverse_lazy('profile')
    # aqui não temos acesso a pk para redirecionar para o perfil
    # então, iremos sobrescrever um método
    
    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.pk])


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('tuites:post_tuite')


# o que for referente a CRUD, geralmente vai pedir um formulário
