from django.shortcuts import render

def blog_view(request):
    return render(request , 'blog/blog-home.html')

def blog_single(request):
    return render(request , 'blog/blog-single.html')
