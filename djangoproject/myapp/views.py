from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse('Hello world')

from .models import Post
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
