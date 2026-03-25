from django.utils import timezone
from urllib import request
from django.views import generic
from django.shortcuts import render

from forum.models import Post

# Create your views here.

class RecentPostsView(generic.ListView):
    template_name = 'forum/forum.html'
    context_object_name = 'recent_posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'forum/post_detail.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now())

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'forum/post_edit.html'
    fields = ['author', 'title', 'text', 'uimage']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.published_date = timezone.now()
        post.save()
        return super().form_valid(form)