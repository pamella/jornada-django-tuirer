from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    # reverse_lazy só será chamado 
    success_url = reverse_lazy('tuites:post_tuite')

    def get_initial(self):
        return {
            'user': self.request.user
        }

    # https://docs.djangoproject.com/en/2.0/ref/contrib/messages/
    def form_valid(self, form):
        messages.success (
            self.request,
            'Você postou um tuite!'
        )
        return super().form_valid(form)


class LikeTuiteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        from_url = self.request.META.get('HTTP_REFERER')
        tuite_pk = kwargs.get('pk')
        user = self.request.user

        if not user.pk:
            return from_url
        
        tuite = Tuite.objects.get(pk=tuite_pk)
        # como o model é manytomany, podemos ter o filtro seguinte:
        if tuite.liked_by.filter(pk=user.pk).exists():
            tuite.liked_by.remove(user)
        else:
            tuite.liked_by.add(user)

        return f'{from_url}#{tuite_pk}'
