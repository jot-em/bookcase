from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=200, verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    category = models.CharField(max_length=200, null=True, verbose_name='Kategoria')
    kind = models.CharField(max_length=200, verbose_name='Rodzaj')
    location = models.CharField(max_length=200, null=True, verbose_name='Lokalizacja')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='Data dodania')
    loan_date = models.DateField(
            blank=True, null=True, verbose_name='Data wypożyczenia')
    due_date = models.DateField(
            blank=True, null=True, verbose_name='Termin oddania')
    returned_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Data oddania')

    lent_to =  models.CharField(blank=True, null=True, max_length=200, verbose_name='Osoba, która pożyczyła')
    lent_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Data pożyczenia')
    lent_back_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Data oddania')

    SOURCE_CHOICES = (('home', 'Zasoby wlasne'), ('library', 'Biblioteka'), ('borrowed', 'Pożyczona od kogoś'), ('others', 'Inne'),)
    source = models.CharField(max_length=200, default='Inne', verbose_name='Źródło')
    STATUS_CHOICES = (('todo', 'Chcę przeczytać'),('inprogress', 'Czytam'),('closed', 'Przeczytałam'))
    status = models.CharField(max_length=200, default = 'todo', verbose_name='Status')
    notes = models.TextField(blank=True, verbose_name='Notatki')
    MARK_CHOICES = (('0', ''), ('1', 'Słaba - nie byłam w stanie doczytać do końca'), ('2', 'Czytałam wiele lepszych'), 
        ('3', 'Dość interesująca'), ('4', 'Podobała mi się'), ('5', 'Rewelacyjna!'))
    mark = models.CharField(max_length=1, default='0', verbose_name='Ocena')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class BookLocation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nazwa lokalizacji')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class BookKind(models.Model):
    name = models.CharField(max_length=200, verbose_name='Rodzaj')
    category = models.CharField(max_length=200, verbose_name='Kategoria')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategoria')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name