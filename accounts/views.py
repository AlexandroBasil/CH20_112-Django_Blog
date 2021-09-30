from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"