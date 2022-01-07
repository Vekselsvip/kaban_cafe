from .models import BookTable
from django.forms import ModelForm, TextInput, Textarea, NumberInput, TimeInput, DateInput


class BookTableForm(ModelForm):
    class Meta:
        model = BookTable
        fields = ['name', 'email', 'time', 'date', 'message', 'people']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email'
            }),
            "date": DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Дата резерваии'
            }),
            "time": TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Время резерваии'
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'сообщение'
            }),
            'people': NumberInput(attrs={
                'type': "number", 'class': "form-control", 'name': "people", 'id': "people", 'placeholder': "количество человек",
        'data-rule': "minlen:1", 'data-msg': "Please enter at least 1 chars"
            })
        }