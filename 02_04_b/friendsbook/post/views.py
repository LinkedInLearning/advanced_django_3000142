from django.http import HttpResponse
from django.template import loader
from .models import Post
from .forms import PostForm


def post_feed(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = add_post(request)
    template = loader.get_template('feed.html')
    posts = Post.objects.all()
    return HttpResponse(template.render({'posts': posts, 'new_post_form': post_form}, request))

def post_detail(request, post_id):
    template = loader.get_template('post_detail.html')
    post = Post.objects.get(id=post_id)
    return HttpResponse(template.render({'post': post}, request))

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


