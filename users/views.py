from django.shortcuts import render
from django.http import render
# Create your views here.
def home(request):
    return render(request, 'users/home.html')
