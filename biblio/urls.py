from django.conf.urls import url
from biblio import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.book_table, name='book_list'),
    url(r'^logowanie/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^wylogowanie/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^ksiazki/$', views.book_list, name='book_list'),
	url(r'^wykaz/$', views.book_table, name='book_table'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/$', views.book_details, name='book_details'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/pozycz/$', views.lend_book, name='lend_book'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/przyjmij_zwrot/$', views.mark_return_book, name='mark_return_book'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/zwroc/$', views.return_book, name='return_book'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/pozyczona', views.popup_lend_success, name='popup_lend_success'),
	url(r'^ksiazka/(?P<pk>[0-9]+)/zwrocona', views.popup_mark_return_success, name='popup_mark_return_success'),
	url(r'^ksiazka/dodaj/$', views.book_new, name = 'book_new'),
	url(r'^ksiazka/edytuj/(?P<pk>[0-9]+)/$', views.book_edit, name = 'book_edit'),
	url(r'^ksiazka/potwierdz-usuniecie/(?P<pk>[0-9]+)/$', views.book_delete_confirm, name = 'book_delete_confirm'),
	url(r'^ksiazka/usun/(?P<pk>[0-9]+)/$', views.book_delete, name = 'book_delete'),
	url(r'^szukaj/$', views.book_search, name='book_search'),
	url(r'^ksiazki/biblioteka$', views.book_library, name='book_library'),


]