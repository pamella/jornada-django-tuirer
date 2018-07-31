from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from users.models import User


class ProfileAccessMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        # mostrando mensagens
        messages.error(
            self.request,
            'Você não pode editar um perfil que não é seu!'
        )
        return redirect('index')

    def dispatch(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        
        if not user == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
        # obs.: super() --> continua o processo, chama o restante dos métodos
