from django import forms
from .models import Us
from .models import Tw

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Us
		fields = ["img","nombre"]

class Tw(forms.ModelForm):

	class Meta:

		model = Tw
		fields = ["id_tw","tw"]
