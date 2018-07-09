from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django_tables2 import RequestConfig
from .models import Book, BookKind
from .tables import BookTable
from .forms import *
from .helpers import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def book_list(request):
	books = Book.objects.exclude(source='library').order_by('author')
	numbered_books = helper_numbered_books_dict(books)
	return render(request, 'biblio/book_list.html', {'book_list': numbered_books, 'title': 'Lista książek - dom'})

def book_table(request):
	table = BookTable(Book.objects.all())
	RequestConfig(request, paginate={'per_page':15}).configure(table)
	return render(request, 'biblio/book_table.html', {'book_table': table, 'title': 'Lista wszystkich książek'})

def book_library(request):
	books = Book.objects.filter(source='library').order_by('author')
	numbered_books = helper_numbered_books_dict(books)
	empty_list = False
	if len(books) == 0:
		empty_list = True
	return render(request, 'biblio/book_list.html', {'book_list': numbered_books, 'title': 'Lista książek z biblioteki', 'empty_library_list': empty_list})

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
			book.category = BookKind.objects.filter(name=book.kind).get().category
			book = form.save(commit=False)
			book.created_date = timezone.now()
			book.save()
			return redirect('book_details', pk=book.pk)
	else:
		form = BookForm(instance=book)
	return render(request, 'biblio/book_edit.html', {'form': form})

def book_delete_confirm(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'biblio/book_confirm_delete.html', {'book': book})

def book_delete(request, pk):
    deleting_book = Book.objects.filter(pk=pk).delete()
    books = Book.objects.all().order_by('author')
    numbered_books = helper_numbered_books_dict(books)
    deleted = True
    return render(request, 'biblio/book_list.html', {'book_list': numbered_books, 'deleted':deleted})

def book_search(request):
	form = BookSearchForm(request.GET)
	books = Book.objects.all().order_by('author')
	if request.method == "GET":
		search_author_query = request.GET.get('author')
		search_title_query = request.GET.get('title')
		search_category_query = request.GET.get('category')
		search_kind_query = request.GET.get('kind')
		search_location_query = request.GET.get('location')
		search_source_query = request.GET.get('source')
		search_status_query = request.GET.get('status')
		search_mark_query = request.GET.get('mark')
		
		filters = {}

		if search_author_query != '':
			filters['author'] = search_author_query

		if search_title_query != '':
			filters['title'] = search_title_query

		if search_category_query != '':
			filters['category'] = search_category_query

		if search_kind_query != '':
			filters['kind'] = search_kind_query

		if search_location_query != '':
			filters['location'] = search_location_query

		if search_source_query != 'None':
			filters['source'] = search_source_query

		if search_status_query != 'None':
			filters['status'] = search_status_query
			
		if search_mark_query != '0':
			filters['mark'] = search_mark_query

		books = Book.objects.filter(**filters)
		numbered_books = helper_numbered_books_dict(books)
		return render(request, 'biblio/book_search.html', {'form': form, 'book_list': numbered_books})

def lend_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookLendForm(request.POST, instance=book)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect('popup_lend_success', pk=book.pk)
	else:
		form = BookLendForm(instance=book, initial={'lent_date':timezone.now()})
	return render(request, 'biblio/popup.html', {'form': form, 'title': 'Pożycz książkę'})

def mark_return_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookLendBackForm(request.POST, instance=book)
		if form.is_valid():
			book = form.save(commit=False)
			book.lent_to = None
			book.save()
			return redirect('popup_mark_return_success', pk=book.pk)
	else:
		form = BookLendBackForm(instance=book, initial={'lent_back_date':timezone.now()})
	return render(request, 'biblio/popup.html', {'form': form, 'title': 'Zaznacz zwrot'})

def return_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		form = BookReturnForm(request.POST, instance=book)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			return redirect('popup_mark_return_success', pk=book.pk)
	else:
		form = BookReturnForm(instance=book, initial={'returned_date':timezone.now()})
	return render(request, 'biblio/popup.html', {'form': form, 'title': 'Oddaj książkę'})

def popup_lend_success(request, pk):
	return render(request, 'biblio/popup_success.html', {'message': 'Książka została pożyczona!'})

def popup_mark_return_success(request, pk):
	return render(request, 'biblio/popup_success.html', {'message': 'Książka została zwrócona!'})
