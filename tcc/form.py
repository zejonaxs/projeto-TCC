from django import forms

from .models import autor, curso, orientador, tcc


class AutorForm(forms.ModelForm):
    class Meta:
        model = autor
        fields = "__all__"

class CursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = "__all__"

class OrientadorForm(forms.ModelForm):
    class Meta:
        model = orientador
        fields = "__all__"

class TccForm(forms.ModelForm):
    class Meta:
        model = tcc
        fields = "__all__"
