from django.contrib.auth import login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from .forms import SigUpForm
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


## Post without pagination
# class MainHome(View):
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         return render(request, 'blog/index.html', context={'posts': posts}


class MainHome(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.get_queryset().order_by('id')
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/index.html', context={'page_obj': page_obj})


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


class SignUpView(View):
    def get(self, request):
        form = SigUpForm()
        return render(request, 'blog/signup.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })
