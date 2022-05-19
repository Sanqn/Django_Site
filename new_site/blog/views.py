from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator


## Post without pagination
# class MainHome(View):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         return render(request, 'blog/index.html', context={'posts': posts}


class MainHome(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/index.html', context={'page_obj': page_obj})
