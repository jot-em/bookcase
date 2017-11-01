from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=200, verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    kind = models.TextField(verbose_name='Gatunek')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='Data dodania')
    loan_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Data wypożyczenia')
    due_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Termin oddania')
    CATEGORIES_CHOICES = (('home', 'Zasoby wlasne'),('library', 'Biblioteka'), ('others', 'Inne'))
    category = models.CharField(max_length=200, default='Inne', verbose_name='Kategoria')
    STATUS = (('todo', 'Chcę przeczytać'),('inprogress', 'Czytam'),('closed', 'Przeczytałam'))
    notes = models.TextField(blank=True, verbose_name='Notatki')

    def publish(self):
        self.save()


    def __str__(self):
        return self.title

