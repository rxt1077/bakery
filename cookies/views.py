from django.shortcuts import render
from .models import Cookie

def index(request):
    context = {'cookies': Cookie.objects.all()}
    return render(request, 'cookies/index.html', context)
