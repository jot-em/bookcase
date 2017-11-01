from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.book_list, name='book_list'),
	url(r'^ksiazki/$', views.book_list, name='book_list'),
	url(r'^wykaz/$', views.book_table, name='book_table'),
	url(r'^ksiazki/(?P<pk>[0-9]+)/', views.book_details, name='book_details'),
	url(r'^ksiazki/dodaj/$', views.book_new, name = 'book_new'),
	url(r'^ksiazki/edytuj/$', views.book_edit, name = 'book_edit'),
	# url(r'^szukaj/$', views.book_search, name='book_search'),
]