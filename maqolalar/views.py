from django.shortcuts import render
from django.views.generic import ListView,DetailView 
from .models import Maqola
# Create your views here.
class MaqolaListView(ListView):
    model = Maqola 
    template_name = 'home.html'
class MaqolaDetailView(DetailView):
    model = Maqola
    template_name = 'maqola_detail.html'
