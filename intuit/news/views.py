from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import PostModel, CategoryModel


class PostListView(ListView):
    queryset = PostModel.active_posts.all()
    context_object_name = "posts"
    paginate_by = 10
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        
        return context


class PostCategoryListView(ListView):
    context_object_name = "posts"
    paginate_by = 10
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(CategoryModel, 
                                        slug = self.kwargs["category"])
        context["title"] = category.title
        
        return context
    
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, 
                                        slug = self.kwargs["category"])
        return category.categories.filter(status="active")

    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(PostModel, slug=post, status='active',
                                date__year=year, date__month=month, date__day=day)
    return render(request, 'news/detail.html', {"title":"Новости", "post": post})




