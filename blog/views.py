from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import PostForm
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)


def post_list(request):
    """
    View for displaying a list of blog articles,
    including sorting and pagination
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
    Class & Method to call the articles details pages.
    """
    template_name = 'blog/post_detail.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {'post': post}
        return render(request, self.template_name, context)


class PostDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    View for deleting an existing blog Article
    """
    model = Post
    template_name = "blog/post_delete.html"
    success_message = 'Article is deleted!'
    success_url = reverse_lazy("blog")

    def test_func(self):
        """
        Check if the current user is admin for
        being able to delete post
        """
        return self.request.user.is_superuser
    
    def get_success_message(self, cleaned_data=None):
        return self.success_message


class PostCreateView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new blog Article
    """
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm
    success_message = "Post has been created"
    success_url = reverse_lazy("blog")

    def test_func(self):
        """
        Check if the current user is a superuser (admin)
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        Custom logic to handle form validation when creating a new blog post
        """
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostEditView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    View for editing an existing Article
    """
    model = Post
    template_name = "blog/post_edit.html"
    form_class = PostForm
    success_message = "Article updated successfully"

    def test_func(self):
        """
        Check if the current user is the author of the post being updated
        """
        post = self.get_object()
        return self.request.user.is_superuser

    def get_success_message(self, cleaned_data=None):
        return self.success_message
