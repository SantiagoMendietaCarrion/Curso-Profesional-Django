from django import forms
from applications.home.models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        widgets = {
            'cantidad':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese texto aquí'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return cantidad
