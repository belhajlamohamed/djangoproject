from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.models import AbstractBaseUser

# Create your views here.
class Ex2View(TemplateView):
    template_name = 'ex2.html'

    def get_context_data(self, **kwargs): 
        context =  super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=2)
        context['data'] = "Context Data for Ex2"
        return context
