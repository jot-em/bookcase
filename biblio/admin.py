from django.contrib import admin
from django import forms
from .models import Book, BookLocation, BookKind, BookCategory

# Register your models here.
class BookKindForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=BookCategory.objects.all(), label='Kategoria', to_field_name="name")
	
	class Meta:
		model = BookKind
		fields = ('name', 'category')

class BookKindAdmin(admin.ModelAdmin):
	form = BookKindForm


admin.site.register(Book)
admin.site.register(BookLocation)
admin.site.register(BookKind, BookKindAdmin)
admin.site.register(BookCategory)