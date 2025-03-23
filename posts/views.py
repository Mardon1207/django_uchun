from django.shortcuts import render
from django.views.generic import ListView
from .models import Talaba

# Create your views here.
class HomePagesViews(ListView):
    model = Talaba
    template_name = 'home.html'