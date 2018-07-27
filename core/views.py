from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from tuites.models import Tuite


def index(request):
    context = {
        "now": datetime.now(),
        'tuites': Tuite.objects.all(),
        # 'tuites': Tuite.objects.search('opa'),
    }

    return render(request, 'home.html', context)