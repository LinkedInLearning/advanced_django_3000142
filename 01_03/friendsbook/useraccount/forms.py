from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'birthday', 'about'] 


    def save(self, user=None):
        user_account = super(UserAccountForm, self).save(commit=False)
        if user:
            user_account.user = user
        user_account.save()
        return user_account
