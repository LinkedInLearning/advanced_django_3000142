from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import Post
from .forms import PostForm
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.vary import vary_on_cookie
import json

def handler_404(request, exception):
    template = loader.get_template('post_404.html')
    return HttpResponse(template.render({'exception': exception}, request), status=404)


@vary_on_cookie
def post_feed(request):
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    post_form = PostForm()
    if request.method == 'POST':
        post_form = add_post(request)
    template = loader.get_template('feed.html')
    # Post.objects.all()
    posts = Post.feed_manager.get_feed(request)
    return HttpResponse(template.render({'posts': posts, 'new_post_form': post_form}, request))

def post_detail(request, post_id):
    template = loader.get_template('post_detail.html')
    post = get_object_or_404(Post, id=post_id)
    return HttpResponse(template.render({'post': post}, request))
    
def draft_post(request):
    if request.method == 'POST':
        request.session['draft_post'] = json.loads(request.body.decode('utf-8'))['post_content']
        return HttpResponse(status=200)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
        
            new_post = Post.objects.create(
                content = form.cleaned_data['content'],
                author = request.user
            )
            new_post.save()
        else:
            print(form.errors)
        return form
    else:
        # Get request
        template = loader.get_template('add_post.html')
        form = PostForm()
        if request.session.get('draft_post'):
            form = PostForm({'content': request.session.get('draft_post')})
        return HttpResponse(template.render({'form': form}, request))




class PostList(ListView):
    model = Post 
    paginate_by=2
    template_name='post_pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['new_post_form'] = PostForm()
        return context

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
        
            new_post = Post.objects.create(
                content = form.cleaned_data['content'],
                author = request.user
            )
            new_post.save()
        else:
            print(form.errors)