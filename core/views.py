from django.shortcuts import render
from django.views.generic import TemplateView

class LandingView(TemplateView):
	template_name = 'base/index.html'

# Create your views here.
