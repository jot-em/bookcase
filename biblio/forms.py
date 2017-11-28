from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	source = forms.ChoiceField(choices=Book.SOURCE_CHOICES, label='Kategoria')
	status = forms.ChoiceField(choices=Book.STATUS_CHOICES, label='Status')
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Jak oceniasz książkę?')
	class Meta:
		model = Book
		fields = ('author', 'title', 'kind',  'source', 'loan_date', 'due_date','status', 'notes', 'mark')

class BookSearchForm(BookForm):
	source = forms.ChoiceField(choices=(('None', ''),)+Book.SOURCE_CHOICES, label='Kategoria')
	status = forms.ChoiceField(choices=(('None', ''),)+Book.STATUS_CHOICES, label='Status')
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Ocena')
	class Meta:
		model = Book
		exclude = ('notes',)

	def __init__(self, *args, **kwargs):
		super(BookSearchForm, self).__init__(*args, **kwargs)
		print(self.fields)
		self.fields['loan_date_from']=forms.DateField(label='Data wypożyczenia od')
		for key, field in self.fields.items():
			self.fields[key].required = False