from django import forms
from .models import Miembro, Membresia
class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = ['nombre', 'descripcion', 'costo_mensual', 'acceso_limitado', 'acceso_entrenador']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'membresia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }