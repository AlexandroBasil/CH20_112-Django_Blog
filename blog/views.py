from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body"]


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


class LandingPageView(TemplateView):
    template_name = "landing_page.html"