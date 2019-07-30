from django.shortcuts import render
from datetime import datetime


def home_view(request):
    context = {'rightnow': datetime.now(),
               'list_items': [1, 2, 3],
               'bool_value': False
               }
    return render(request, 'index.html', context=context)
