from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'app/index.html')


def product(request):
    return render(request,'app/product.html')

def blog(request):
    return render(request,'app/blog.html')

def contact(request):
    return render(request,'app/contact.html')

def login(request):
    return render(request,'app/login.html')