from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog

def home(request):
    data = Blog.objects
    datas = Blog.objects.all()
    paginator = Paginator(datas,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'data':data, 'posts':posts})
