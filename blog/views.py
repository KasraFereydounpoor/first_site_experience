from django.shortcuts import render , get_list_or_404
from blog.models import Post
def blog_view(request):
    posts = Post.objects.filter(status =1)
    context = {'posts': posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request , pid ):
    post = get_list_or_404(Post , pk=pid)
    context = {'post': post}
    return render(request , 'blog/blog-single.html', context)

def test(request , pid):
    #posts = Post.objects.all()
    post = get_list_or_404(Post , pk=pid)
    context = {'post': post}
    return render(request , 'test.html' , context)