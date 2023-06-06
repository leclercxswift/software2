from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Publicaciones
class UserRegisterForm(UserCreationForm):
 
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields }
class PublicacionesForm(forms.ModelForm):
    content=forms.CharField(label='',widget=forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Que está pasando',
                'style': 'background-color: #bbb; color: #000; border-radius: 5px;',
          
                'oninput': "this.style.height = ''; this.style.height = this.scrollHeight + 'px';",
            
            }),required=True)
    class Meta:
        model= Publicaciones
        fields=['content']