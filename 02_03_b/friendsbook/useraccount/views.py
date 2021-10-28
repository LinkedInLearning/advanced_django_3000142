from django.http.response import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from .models import UserAccount
from django.apps import apps
from .forms import UserAccountForm



def useraccount_edit(request, useraccount_id):
    useraccount = get_object_or_404(UserAccount, id=useraccount_id)
    
    if not request.user or (request.user.id != useraccount.user.id):
        return HttpResponseForbidden()

    template = loader.get_template('useraccount_edit.html')

    if request.method == "POST":
        form = UserAccountForm(request.POST, request.FILES, instance=useraccount)
        if form.is_valid():
            form.save()
            return HttpResponse(template.render({'profile_edit_form': UserAccountForm(initial=model_to_dict(useraccount)), 'useraccount': useraccount}, request))
        else:
            return HttpResponse(template.render({
                'profile_edit_form': UserAccountForm(initial=model_to_dict(useraccount)),
                'useraccount': useraccount,
                'errors': form.errors
                }, request))
    else:
        return HttpResponse(template.render({'profile_edit_form': UserAccountForm(initial=model_to_dict(useraccount)), 'useraccount': useraccount}, request))
    
