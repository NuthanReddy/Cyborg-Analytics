from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse


def home(request):
    if not request.user.is_authenticated():
        return render(request, 'website/index.html')
    else:
        user = request.user
        return render(request, 'website/index.html')

