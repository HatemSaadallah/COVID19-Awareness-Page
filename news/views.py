from typing import List
from django.db.models import query
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class StartingPageView(ListView):
    template_name = "news/index.html"
    model = Post
    ordering = ["date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:2]
        return data

class AllNewsView(ListView):
    template_name = "news/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class AllImages(ListView):
    template_name = "news/all-images.html"
    model = Post
    ordering = ["date"]
    context_object_name = "all_images"

class RegisterForm(ListView):
    template_name = "news/register-form.html"
    model = Post
    ordering = ["date"] 

class SingleNewView(DetailView):
    template_name = "news/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context