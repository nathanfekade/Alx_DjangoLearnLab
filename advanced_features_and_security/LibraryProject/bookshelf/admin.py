from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "publication_year")
  search_fields = ('author', 'author')
  list_filter = ('publication_year',)

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'date_of_birth', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
  search_fields = ('username', 'email')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)