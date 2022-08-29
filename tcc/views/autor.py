from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tcc.form import AutorForm
from tcc.models import autor


class AutorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = autor
    form_class = AutorForm
    success_message = 'Autor cadastrado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores - TCC'
        context['descricao'] = 'Cadastro de Autor(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class AutorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = autor
    form_class = AutorForm
    success_message = 'Autor(a) atualizado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Autores - TCC'
        context['descricao'] = 'Editar Autor(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class AutorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = autor
    success_message = 'Autor(a) excluído com sucesso!'
    template_name = "form/form-excluir.html"
    success_url = reverse_lazy("listar_autores")

class AutorList(ListView):
    model = autor
    template_name = "listar/autores.html"
