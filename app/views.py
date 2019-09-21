from django.shortcuts import render

# Create your views here.
from app.models import Data


def index(request):
    last = Data.objects.last()
    return render(request, 'index.html', {"data": last.message})
