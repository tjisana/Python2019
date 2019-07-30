from django.shortcuts import render

# Create your views here.
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    queryset = Article.objects.all()
    form_class = ArticleModelForm


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):
    queryset = Article.objects.all()
