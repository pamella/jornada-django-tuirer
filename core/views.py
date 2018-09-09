from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from tuites.models import Tuite


def index(request):
    context = {
        "now": datetime.now(),
        'tuites': Tuite.objects.all().order_by('-date_created'),
        # 'tuites': Tuite.objects.search('opa'),
    }

    return render(request, 'home.html', context)
