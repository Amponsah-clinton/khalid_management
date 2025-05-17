from .models import Worker
from django import forms

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'phone', 'gh_card', 'email', 'profile_picture', 'groups', 'is_leader']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'is_leader':
                field.widget = forms.Select(choices=[(True, 'Yes'), (False, 'No')])
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control form-control-file'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item', 'unit_price']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unit price',
                'step': '0.01'
            }),
        }
