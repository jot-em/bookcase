from django import forms
from .models import Book, BookLocation, BookCategory, BookKind
from django.db.models.functions import Lower

class BookForm(forms.ModelForm):
	kind = forms.ModelChoiceField(queryset=BookKind.objects.order_by(Lower('name')), label='Rodzaj', to_field_name='name')
	source = forms.ChoiceField(choices=Book.SOURCE_CHOICES, label='Źródło')
	status = forms.ChoiceField(choices=Book.STATUS_CHOICES, label='Status')
	location = forms.ModelChoiceField(queryset=BookLocation.objects.order_by(Lower('name')), label='Lokalizacja', to_field_name='name', required=False)
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Jak oceniasz książkę?')
	class Meta:
		model = Book
		fields = ('author', 'title', 'kind',  'source', 'location', 'loan_date', 'due_date', 'returned_date', 'status', 'notes', 'mark')

class BookSearchForm(BookForm):
	source = forms.ChoiceField(choices=(('None', ''),)+Book.SOURCE_CHOICES, label='Źródło')
	status = forms.ChoiceField(choices=(('None', ''),)+Book.STATUS_CHOICES, label='Status')
	mark = forms.ChoiceField(choices=Book.MARK_CHOICES, label='Ocena')
	category = forms.ModelChoiceField(queryset=BookCategory.objects.all(), label='Kategoria', to_field_name='name')
	class Meta:
		model = Book
		exclude = ('notes',)

	def __init__(self, *args, **kwargs):
		super(BookSearchForm, self).__init__(*args, **kwargs)
		print(self.fields)
		self.fields['loan_date_from']=forms.DateField(label='Data wypożyczenia od')
		for key, field in self.fields.items():
			self.fields[key].required = False


class BookLendForm(forms.ModelForm):
	lent_to = forms.CharField(label='Komu pożyczasz?',required=True)
	class Meta:
		model = Book
		fields = ('lent_to','lent_date',)

class BookLendBackForm(forms.ModelForm):
	lent_back_date = forms.DateTimeField(label='Data oddania',required=False)
	class Meta:
		model = Book
		fields = ('lent_back_date',)

class BookReturnForm(forms.ModelForm):
	returned_date = forms.DateTimeField(label='Data oddania',required=False)
	class Meta:
		model = Book
		fields = ('returned_date',)