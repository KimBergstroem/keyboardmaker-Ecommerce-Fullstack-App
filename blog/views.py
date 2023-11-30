from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    """
    View for displaying a list of blog posts on the homepage,
    including sorting and search queries
    """
    posts = Post.objects.filter(status=1)
    query = None  
    sort = None
    direction = None
    paginate_by = 4

    if request.GET:
        # Check and apply sorting parameters
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'created_on':
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
            else:
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                posts = posts.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('blog'))

            queries = Q(title__icontains=query) | Q(excerpt__icontains=query)
            posts = posts.filter(queries)

    # Create a string representation of the current sorting for display
    current_sorting = f'{sort}_{direction}'

    # Pagination 
    paginator = Paginator(posts, paginate_by)
    page = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'query': query,
        'current_sorting': current_sorting,
        'paginate_by': paginate_by,
    }
    return render(request, 'blog/blog.html', context)


class PostDetail(View):
    """
    Class & Method to call the post details pages.
    """
    template_name = 'blog/post_detail.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {'post': post}
        return render(request, self.template_name, context)
