from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django_tables2 import RequestConfig
from .models import Book
from .tables import BookTable
from .forms import BookForm

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
    return render(request, 'blog/book_list.html', {'book_list': books, 'deleted':deleted})
