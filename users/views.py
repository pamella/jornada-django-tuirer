from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView    # updateview --> usada para editar um model que já existe

from users.mixins import ProfileAccessMixin
from users.models import User


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
        return reverse_lazy('profile', args=[self.object.pk])

# o que for referente a CRUD, geralmente vai pedir um formulário