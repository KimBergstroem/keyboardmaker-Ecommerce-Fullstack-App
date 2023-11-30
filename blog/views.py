from django.shortcuts import render
from .models import Post


def post_list(request):
    """
    View for displaying a list of blog posts on the homepage
    """
    posts = Post.objects.filter(status=1).order_by("-created_on")
    
    context = {
        'posts': posts,
        'paginate_by': 6,
    }

    return render(request, 'blog/blog.html', context)
