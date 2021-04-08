from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special'):
        characters.extend(list('!@$%^&*()'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    Length = int(request.GET.get('Length', 12))

    thepassword = ''

    for x in range(Length):
        thepassword += random.choice(characters)
    return render(request, 'generator/Password.html', {'password': thepassword})




# Create your views here.
