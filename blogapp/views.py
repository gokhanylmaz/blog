from django.shortcuts import render
from blogapp.models import Blog


# Create your views here.
def home(request):
    return render(request, 'index.html')
def blog(request):
    context = {
        "blogs": Blog.objects.order_by('-pub_date')
    }
    return render(request, 'blog.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def details(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'details.html',{ 
        "blogs": blog
    })
