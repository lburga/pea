from django.shortcuts import render
from .choices import (get_pea,)

def login(request):
	return render(request, 'login.html')

def main(request):
	context = get_pea()
	return render(request, 'main.html', context)