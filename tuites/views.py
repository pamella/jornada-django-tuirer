from django.shortcuts import render
from tuites.models import Tuite


def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando formulário!')
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