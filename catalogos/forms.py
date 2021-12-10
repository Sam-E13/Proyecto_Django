from django import forms
from django.forms.models import fields_for_model
from .models import Cliente, Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter (self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter (self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

'''

    class Meta:
        model = Producto
        fields = [
            'descripcion',
            'precio',
            'categoria'
        ] 
'''