from django.utils.translation import pgettext, ugettext_lazy as _, ugettext
from django import forms

from allauth.account.forms import SetPasswordField, PasswordField
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    name = forms.CharField(label=_("Name"),
                           max_length=64,
                           min_length=3,
                           widget=forms.TextInput(attrs={'placeholder': 'Name',}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'placeholder': _('E-mail address')}))
    password1 = SetPasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    confirmation_key = forms.CharField(max_length=40,
                                       required=False,
                                       widget=forms.HiddenInput())

    def custom_signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.save()

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(SignupForm, self).clean()
        if "password1" in self.cleaned_data and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
                raise forms.ValidationError(_("Passwords must match."))
        if User.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError(_("Email address already in use."))
        return self.cleaned_data

    def save(self, request):
        print('Accont form save')
        adapter = get_adapter()
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # TODO: Move into adapter `save_user` ?
        setup_user_email(request, user, [])

        return user
