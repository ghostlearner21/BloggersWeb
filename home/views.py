from datetime import date

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': date.today()}


class NotesLoginView(LoginView):
    template_name = 'home/login.html'


class NotesLogoutView(LogoutView):
    template_name = 'home/logout.html'


class NotesSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/notes/list'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args, **kwargs)

