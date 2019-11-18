from django.shortcuts import render
from django.http import HttpResponse
from .models import Cookie
from .forms import BakerForm

def index(request):
    context = {'cookies': Cookie.objects.all()}
    return render(request, 'cookies/index.html', context)
    
def baker(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BakerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thanks for baking cookies.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BakerForm()
    return render(request, 'cookies/baker.html', {'form': form})
