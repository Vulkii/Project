from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from .models import Task


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "kogda","who"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "kogda": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "who": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите своё имя'
            }),
        }