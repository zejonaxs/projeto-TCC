from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tcc.form import TccForm
from tcc.models import tcc


class TccCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = tcc
    form_class = TccForm
    success_message = 'tcc cadastrado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_tccs")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'tccs - TCC'
        context['descricao'] = 'Cadastro de tcc'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = tcc
    form_class = TccForm
    success_message = 'tcc atualizado com sucesso!'
    template_name = "form/form.html"
    success_url = reverse_lazy("listar_tccs")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'tccs - TCC'
        context['descricao'] = 'Editar tcc'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = tcc
    success_message = 'tcc excluído com sucesso!'
    template_name = "form/form-excluir.html"
    success_url = reverse_lazy("listar_tccs")

class TccList(ListView):
    model = tcc
    template_name = "listar/tccs.html"

class TccDetail(DetailView):
    model = tcc
    template_name = "detalhes/tcc.html"
class TccHome(ListView):
    model = tcc
    template_name = "index.html"
