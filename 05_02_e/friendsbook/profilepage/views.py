from django.http.response import HttpResponse
from django.template import loader

from .models import ProfilePage
from django.apps import apps

import datetime

def profile_detail(request, profilepage_id):
    template = loader.get_template('profilepage.html')
    profile = ProfilePage.objects.get(id=profilepage_id)
    posts = []
    own_profile = False
    if profile.content_type.model == 'useraccount':
        Post = apps.get_model('post', 'Post')
        posts = Post.objects.filter(author=profile.subject.user)
        own_profile = request.user and (request.user.id == profile.subject.user.id)
    return HttpResponse(template.render({'profile': profile, 'posts': posts, 'own_profile': own_profile, 'seconds_since': get_seconds_since(profile.subject.birthday)}, request))

def get_seconds_since(date):
        return (datetime.date.today() - date).total_seconds()
