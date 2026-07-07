from django import forms
from .models import MensagemContato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato

        fields = ['nome', 'email', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escreva sua mensagem, crítica ou sugestão...'}),
        }
