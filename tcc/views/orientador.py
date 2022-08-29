from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tcc.form import OrientadorForm
from tcc.models import orientador


class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = orientador
    form_class = OrientadorForm
    success_message = 'orientador cadastrado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'orientadores - TCC'
        context['descricao'] = 'Cadastro de orientador(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = orientador
    form_class = OrientadorForm
    success_message = 'orientador(a) atualizado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'orientadores - TCC'
        context['descricao'] = 'Editar orientador(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = orientador
    success_message = 'orientador(a) excluído com sucesso!'
    template_name = "form/form-excluir.html"
    success_url = reverse_lazy("listar_orientadores")

class OrientadorList(ListView):
    model = orientador
    template_name = "listar/orientadores.html"
