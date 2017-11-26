from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	source = forms.ChoiceField(choices=Book.SOURCE_CHOICES, label='Kategoria')
	status = forms.ChoiceField(choices=Book.STATUS_CHOICES, label='Status')
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Jak oceniasz książkę?')
	class Meta:
		model = Book
		fields = ('author', 'title', 'kind',  'source', 'loan_date', 'due_date','status', 'notes', 'mark')
