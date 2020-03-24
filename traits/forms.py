from django import forms
from .models import Trait

class TraitForm(forms.ModelForm):
	class Meta:
		model = Trait
		fields = ['title', 'is_mapped']