from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# updateview --> usada para editar um model que já existe
from django.views.generic import (CreateView, DetailView, RedirectView,
                                  UpdateView)

from users.forms import UserCreationForm, UserSignupForm
from users.mixins import ProfileAccessMixin
from users.models import User

# https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#detailview
# a ordem dos Mixins importa. o quanto antes, maior a importância

# o que for referente a CRUD, geralmente vai pedir um formulário


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


class UserFollowView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        profile_pk = kwargs.get('pk')
        profile = User.objects.get(pk=profile_pk)
        request_user = self.request.user
        request_user_has_followed = request_user.following.filter(pk=profile_pk).exists()
        # import ipdb ; ipdb.set_trace()
        
        # caso o user logado siga o perfil
        if request_user_has_followed:
            request_user.following.remove(profile)
            profile.followers.remove(request_user)
        # caso o user logado não siga o perfil
        else:
            request_user.following.add(profile)
            profile.followers.add(request_user)
        
        return reverse_lazy('users:profile', args=[profile_pk])
