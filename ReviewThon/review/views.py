from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

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

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('home')
        return render(request, 'new.html', {'form':form})
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def update (request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = BlogPost(request.POST,request.FILES, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'new.html', {'form':form})

def delete (request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')
