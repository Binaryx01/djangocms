from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()  # Corrected line
    return render(request, 'sorrycmsapp/index.html', {'posts': posts})
