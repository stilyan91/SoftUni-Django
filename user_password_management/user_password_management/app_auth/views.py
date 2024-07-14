from ..web.models import  Profile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import views, login, authenticate, get_user_model
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import mixins as auth_mixins


UserModel = get_user_model()
class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password please")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works'

    def save(self, commit=True):
        user = super().save(commit)
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        profile = Profile(first_name=first_name, last_name=last_name,
                          user=user)

        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

class RegisterView(generic.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # Static way
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result

    # def get_form_kwargs(self):
    #     if condition1:
    #         return ConditionForm
    #     elif condition2:
    #         return ConditionFORM2
    #     else:
    #         return ConditionForm3

# Dynamic way to get success_url
#     def get_success_url(self):
#         pass


class LoginUserView(views.LoginView):
    template_name = 'app_auth/login.html'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['initial'] = {
    #         'password': 'aaaa1234',
    #     }
    #     return kwargs


class LogoutView(views.LogoutView):
    pass




@login_required
def func_view(request):
    pass


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, generic.TemplateView):
    pass


class UsersListView(auth_mixins.LoginRequiredMixin, generic.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'


