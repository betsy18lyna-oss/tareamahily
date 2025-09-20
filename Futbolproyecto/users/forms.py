from django import forms
from .models import Equipo
from django.contrib.auth.forms import UserCreationForm 

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) 