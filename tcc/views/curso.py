from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tcc.form import CursoForm
from tcc.models import curso


class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = curso
    form_class = CursoForm
    success_message = 'curso cadastrado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'cursos - TCC'
        context['descricao'] = 'Cadastro de curso'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = curso
    form_class = CursoForm
    success_message = 'curso atualizado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'cursos - TCC'
        context['descricao'] = 'Editar curso'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = curso
    success_message = 'curso excluído com sucesso!'
    template_name = "form/form-excluir.html"
    success_url = reverse_lazy("listar_cursos")

class CursoList(ListView):
    model = curso
    template_name = "listar/cursos.html"
