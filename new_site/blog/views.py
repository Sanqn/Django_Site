from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Comment
from .forms import SigUpForm, SignInForm, FeedBackForm, CommentForm
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from taggit.models import Tag
from django.views.generic import ListView, DetailView


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


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        common_tags = Post.tag.most_common()
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', context={
            'post': post,
            'common_tags': common_tags,
            'last_posts': last_posts,
            'comment_form': comment_form,
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.cteate(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'blog/post_detail.html', context={
            'comment_form': comment_form
        })



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
        return render(request, 'blog/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request):
        form = SignInForm
        return render(request, 'blog/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog/signin.html', context={
            'form': form,
        })


class FeedbackView(View):
    def get(self, request):
        feed = FeedBackForm()
        return render(request, 'blog/contact.html', context={
            'feed': feed,
            'title': 'Message me'
        })

    def post(self, request):
        feed = FeedBackForm(request.POST)
        if feed.is_valid():
            name = feed.cleaned_data['name']
            from_email = feed.cleaned_data['email']
            subject = feed.cleaned_data['subject']
            message = feed.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, [from_email])
            except BadHeaderError:
                return HttpResponse('Invalid title')
            return HttpResponseRedirect('success')
        return render(request, 'blog/contact.html', context={
            'feed': feed,
        })

class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/success.html', context={
            'title': 'Thanks'
        })

class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        search = self.request.GET.get('q')
        results = ''
        if search:
            results = Post.objects.filter(
                Q(h1__icontains=search) | Q(content__icontains=search)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        results_page_obj = paginator.get_page(page_number)
        return render(request, 'blog/search.html', context={
            'title': 'search',
            'results_page_obj': results_page_obj,
            'count': len(results)
        })

class TagView(View):
    def get(self, request, slug,  *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tag=tag)
        common_tags = Post.tag.most_common()
        return render(request, 'blog/tag.html', context={
            'title': f'#Tag {tag}',
            'posts': posts,
            'common_tags': common_tags
        })
