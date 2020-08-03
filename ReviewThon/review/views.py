from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

def home(request):
    data = Blog.objects
    datas = Blog.objects.all()
    paginator = Paginator(datas,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'data':data, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})
