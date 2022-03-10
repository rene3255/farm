from django.shortcuts import render
from .models import Rabbit

def rabbit_list(request):
  rabbits = Rabbit.objects.all()
  return render(request,
          'rabbit/list/list.html',
          {'rabbits': rabbits})
          
