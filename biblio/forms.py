from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	category = forms.ChoiceField(choices=Book.CATEGORIES_CHOICES, label='Kategoria')
	status = forms.ChoiceField(choices=Book.STATUS_CHOICES, label='Status')
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Jak oceniasz książkę?')
	class Meta:
		model = Book
		fields = ('author', 'title', 'kind', 'category', 'status', 'notes', 'mark')