from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    kind = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    loan_date = models.DateTimeField(
            blank=True, null=True)
    due_date = models.DateTimeField(
            blank=True, null=True)
    CATEGORIES_CHOICES = (('home', 'Zasoby wlasne'),('library', 'Biblioteka'), ('others', 'Inne'))
    categories = models.CharField(max_length=200, default='Inne')
    STATUS = (('todo', 'Chcę przeczytać'),('inprogress', 'Czytam'),('closed', 'Przeczytałam'))
    notes = models.TextField(blank=True)

    def publish(self):
        self.save()


    def __str__(self):
        return self.title