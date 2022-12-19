from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, DetailView, CreateView, UpdateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm


# Create your views here.

class AuthorizedView(LoginRequiredMixin):
    template_name = 'home/authorized.html'
    login_url = '/login'


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/notes_details.html'
    context_object_name = "note"
    login_url = '/login'


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    template_name = 'notes/notes_form.html'
    form_class = NotesForm
    success_url = '/notes/list'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes/list'
    login_url = '/login'


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'notes/notes_delete.html'
    success_url = '/notes/list'
    login_url = '/login'
