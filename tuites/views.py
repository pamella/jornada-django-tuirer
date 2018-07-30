from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    # reverse_lazy só será chamado 
    success_url = reverse_lazy('post_tuite')

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


# código abaixo não utilizado:

def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando formulário!')
        # print(request.POST)
        # content name do input do form
        content = request.POST.get('content', None)
        if content.isspace() or content == '':
            context['error'] = 'Tuite não pode estar vazio'
        else:
            tuite = Tuite.objects.create(
                content=content,
                author=request.user,
            )
            context['success_message'] = f'Seu Tuite de conteúdo {tuite.content} foi enviado'

    return render(request, 'post_tuite.html', context)
