from django.urls import path
from django.views.generic import TemplateView
from .views import Ex2View
from . import views

app_name = 'website'
urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'custom-title'})),
    path('ex2', Ex2View.as_view(), name='ex2'),
    
    
]
