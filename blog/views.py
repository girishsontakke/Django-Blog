from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-date_posted")
    template_name = "blog/home.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
