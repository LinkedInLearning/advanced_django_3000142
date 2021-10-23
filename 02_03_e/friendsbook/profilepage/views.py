from django.http.response import HttpResponse, HttpResponseForbidden
from django.template import loader

from .models import ProfilePage
from django.apps import apps

import datetime


def profile_detail(request, profilepage_id):
    template = loader.get_template('profilepage.html')
    profile = ProfilePage.objects.get(id=profilepage_id)
    Post = apps.get_model('post', 'Post')
    posts = Post.objects.filter(author=profile.user_account.user)
    own_profile = request.user and (request.user.id == profile.user_account.user.id)
    return HttpResponse(template.render({'profile': profile, 'posts': posts, 'own_profile': own_profile}, request))


