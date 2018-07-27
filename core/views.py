from django.shortcuts import render
from django.http import HttpResponse
from core.helpers import get_character_name, ip_info
from datetime import datetime

# Create your views here.

#def index(request):
#    nome = 'Pam'
#    return HttpResponse(f'Sua página carregou, {nome}.')

#def index(request):
#    nome = get_character_name(5)
#    return HttpResponse(f'Olá, {nome}')

#def index(request):
#    country = ip_info('country_name')
#    flag = ip_info('flag')
#    flag_image =f'<img src="{flag}" width="120" />'
#    return HttpResponse(
#        f'Olá do <b>{country} </b>! <br>{flag_image}</br>'
#    )

# def index(request):
#     country = ip_info('country_name')
#     flag = ip_info('flag')
#     flag_image =f'<img src="{flag}" width="120" />'

#     context = {
#         'country': country,
#         'flag': flag
#     }

#     return render(request, 'index.html')

def index(request):
    context = {
        "now": datetime.now(),
    }

    return render(request, 'home.html', context)