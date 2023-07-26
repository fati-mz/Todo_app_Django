from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    body = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
