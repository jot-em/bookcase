from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django_tables2 import RequestConfig
from .models import Book
from .tables import BookTable
from .forms import BookForm, BookSearchForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def book_list(request):
	books = Book.objects.all().order_by('author')
	return render(request, 'biblio/book_list.html', {'book_list': books})

def book_table(request):
	table = BookTable(Book.objects.all())
	RequestConfig(request, paginate={'per_page':15}).configure(table)
	return render(request, 'biblio/book_table.html', {'book_table': table})

def book_details(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'biblio/book_details.html', {'book': book})

def book_new(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.created_date = timezone.now()
			book.save()
			return redirect('book_details', pk=book.pk)
	else:
		form = BookForm()
	return render(request, 'biblio/book_new.html', {'form': form})

def book_edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			book = form.save(commit=False)
			book.created_date = timezone.now()
			book.save()
			return redirect('book_details', pk=book.pk)
	else:
		form = BookForm(instance=book)
	return render(request, 'biblio/book_edit.html', {'form': form})

def book_delete(request, pk):
    deleting_book = Book.objects.filter(pk=pk).delete()
    books = Book.objects.all().order_by('author')
    deleted = True
    return render(request, 'biblio/book_list.html', {'book_list': books, 'deleted':deleted})

def book_search(request):
	form = BookSearchForm(request.GET)
	books = Book.objects.all().order_by('author')
	if request.method == "GET":
		search_author_query = request.GET.get('author')
		search_title_query = request.GET.get('title')
		search_kind_query = request.GET.get('kind')
		search_source_query = request.GET.get('source')
		search_status_query = request.GET.get('status')
		search_mark_query = request.GET.get('mark')
		
		filters = {}

		if search_author_query != '':
			filters['author'] = search_author_query

		if search_title_query != '':
			filters['title'] = search_title_query

		if search_kind_query != '':
			filters['kind'] = search_kind_query

		if search_source_query != 'None':
			filters['source'] = search_source_query

		if search_status_query != 'None':
			filters['status'] = search_status_query
			
		if search_mark_query != '0':
			filters['mark'] = search_mark_query


		print(filters)



		books = Book.objects.filter(**filters)
		return render(request, 'biblio/book_search.html', {'form': form, 'book_list': books})
