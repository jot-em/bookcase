import django_tables2 as tables
from .models import Book
import itertools

class BookTable(tables.Table):
	row_number = tables.Column(empty_values=(), verbose_name = 'Lp.')
	class Meta:
		model = Book
		template = 'django_tables2/bootstrap.html'
		fields = ('row_number', 'author', 'title', 'kind', 'created_date', 'loan_date', 'due_date', 'returned_date', 'lent_to', 'lent_date', 'lent_back_date', 'source', 'status', 'mark')
		
	def __init__(self, *args, **kwargs):
		super(BookTable, self).__init__(*args, **kwargs)
		self.counter = itertools.count()

	def render_row_number(self):
		return next(self.counter)+1