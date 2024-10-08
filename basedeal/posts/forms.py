from django import forms
from django.forms import EmailInput, Textarea, TextInput
# from django.utils.translation import gettext_lazy as _
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('author', 'text', 'phone_number', 'e_mail',)
        widgets = {
            'text': Textarea(attrs={'style': 'width: 100%;', 'rows': 5, 'placeholder': 'ЗАДАЧА | КУРС ПОВЫШЕНИЯ КВАЛИФИКАЦИИ'},),
            'e_mail': EmailInput(attrs={'style': 'width: 100%;', 'placeholder': 'test@example.com'}),
            'phone_number': TextInput(attrs={'style': 'width: 100%;', 'placeholder': '+79785558989'}),
            'author': TextInput(attrs={'style': 'width: 100%;', 'placeholder': 'ИМЯ'}),          
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
